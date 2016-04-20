# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.db import connection, ProgrammingError


class Command(BaseCommand):
    args = ''
    help = 'Purge deprecated model users type and migrate to MoocUser model'
    c = connection.cursor()
    tim_users = if_users = []


    def user_table_count(self, user_model_name):
        count = 0
        try:
            self.c.execute('select count(*) from %suser' % user_model_name)
            count = self.c.fetchone()[0]
            tb_exist = True
        except ProgrammingError:
            tb_exist = False
        return [count, tb_exist]

    def alter_old_table(self):
        old_model = ['accounts_timtec', 'timtec'] if self.tim_users > self.if_users else ['ifs_if', 'if']
        self.c.execute('alter table %suser rename to accounts_moocuser' % old_model[0])
        self.c.execute('alter table %suser_groups rename to accounts_moocuser_groups' % old_model[0])
        self.c.execute('alter table accounts_moocuser_groups rename "%suser_id" to "moocuser_id"' % old_model[1])
        self.c.execute(
            'alter table %suser_user_permissions rename to accounts_moocuser_user_permissions' % old_model[0])
        self.c.execute(
            'alter table accounts_moocuser_user_permissions rename "%suser_id" to "moocuser_id"' % old_model[1])
        self.c.execute('alter table %suser_id_seq rename to accounts_moocuser_id_seq' % old_model[0])
        self.c.execute('alter table %suser_groups_id_seq rename to accounts_moocuser_groups_id_seq' % old_model[0])
        self.c.execute(
            'alter table %suser_user_permissions_id_seq rename to accounts_moocuser_user_permissions_id_seq' %
            old_model[0])
        self.c.execute('alter table core_class_students rename "%suser_id" to "moocuser_id"' % old_model[1])
        self.c.execute('alter table core_professormessage_users rename "%suser_id" to "moocuser_id"' % old_model[1])


        if old_model[1] == 'if':
            self.c.execute(
                "delete from accounts_moocuser_groups where exists (select 1 from accounts_moocuser" +
                " where COALESCE(email, '') = '')")
            self.c.execute(
                "delete from accounts_moocuser_user_permissions where exists (select 1 from accounts_moocuser" +
                " where COALESCE(email, '') = '')")
            self.c.execute("delete from accounts_moocuser where COALESCE(email, '') = ''");


    def drop_user_model(self, model):
        try:
            self.c.execute('drop table %suser' % model)
            self.c.execute('drop table %suser_groups' % model)
            self.c.execute('drop table %suser_user_permissions' % model)
            self.c.execute('drop table %suser_id_seq' % model)
            self.c.execute('drop table %suser_groups_id_seq' % model)
            self.c.execute('drop table %suser_user_permissions_id_seq' % model)
        except ProgrammingError:
            pass


    def handle(self):
        self.tim_users = self.user_table_count('accounts_timtec')
        self.if_users = self.user_table_count('ifs_if')

        if self.tim_users[0] or self.if_users[0]:
            mooc_users = self.user_table_count('accounts_mooc')
            if mooc_users[1] and not mooc_users[0]:  # A tabela existe e não tem usuários
                self.drop_user_model('accounts_mooc')
                self.alter_old_table()
            elif not mooc_users[1]:  # A tabela não existe
                self.alter_old_table()

            if self.tim_users[1]:
                self.drop_user_model('accounts_timtec')
            if self.if_users[1]:
                self.drop_user_model('ifs_if')