import pytest
from model_mommy import mommy


@pytest.mark.django_db
def test_course_material(admin_client, user):
    from course_material.models import CourseMaterial
    course = mommy.make('Course', name='Test Course', slug='dbsql')
    mommy.make('Lesson', course=course, slug='lesson')
    # course_material = mommy.make('CourseMaterial', course=course, text='foobar**bold**')
    course_material = CourseMaterial.objects.get(course=course)
    course_material.text = 'foobar**bold**'
    course_material.save()

    response = admin_client.get('/course/' + course.slug + '/material/')

    assert response.status_code == 200
    assert course_material.text[:6].encode('utf-8') in response.content
    # Test Markdown rendering
    assert '<strong>bold</strong>'.encode('utf-8') in response.content


@pytest.mark.django_db
def test_file_upload(rf, user):
    from django.conf import settings
    from course_material.views import FileUploadView
    from course_material.models import CourseMaterial
    import os

    file_name = settings.MEDIA_ROOT + '/dbsql/dummy_file.txt'
    if os.path.exists(file_name):
        os.remove(file_name)

    course = mommy.make('Course', name='Test Course', slug='dbsql')
    # course_material = mommy.make('CourseMaterial', course=course, text='foobar**bold**')
    course_material = CourseMaterial.objects.get(course=course)

    with open('course_material/tests/dummy_file.txt') as fp:
        request = rf.post('/course_material/file_upload/dbsql', {'file': fp, 'course_material': course_material.id})
        request.user = user
        view = FileUploadView(request=request)
        view.kwargs = {'slug': 'dbsql'}
        response = view.post(request)

    assert response.status_code == 200
    assert os.path.exists(file_name)
    assert course_material.files.all()[0].file.name == 'dbsql/dummy_file.txt'
    if os.path.exists(file_name):
        os.remove(file_name)
