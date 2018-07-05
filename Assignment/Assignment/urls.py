from resources.create_user import CreateUser
from resources.user_login import UserLogin
from resources.fetch_courses import FetchCourses
from resources.course_mapp import CourseMapp
from resources.creation_of_course import CreationOfCourse
from resources.delete_course import DeleteCourse
from resources.delete_student import DeleteStudent
from resources.unassign_course import UnassignCourse
from resources.students_by_course import StudentByCourse
from resources.students_fetch import StudentsFetch


def pages(api):
    """
    This contains the urls for all the pages
    :param api: Flask-restful api object
    :return: None
    """
    api.add_resource(CreateUser, '/User_create')
    api.add_resource(UserLogin, '/login')
    api.add_resource(FetchCourses, '/fetch_courses')
    api.add_resource(CourseMapp, '/enable_courses')
    api.add_resource(CreationOfCourse, '/Course_create')
    api.add_resource(DeleteCourse, '/delete_course')
    api.add_resource(UnassignCourse, '/Unassign_Course')
    api.add_resource(DeleteStudent, '/delete_student')
    api.add_resource(StudentByCourse, '/course_by_student/<course_id>')
    api.add_resource(StudentsFetch, '/fetch_all_student/<username>')
