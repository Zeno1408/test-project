import streamlit as st
import requests

# Define the API endpoint
student_id = "c7fada79-826b-4a39-90d5-4f715198463e"
GET_STUDENTS_URL = "http://127.0.0.1:8000/students"
DELETE_STUDENT_URL = f"http://127.0.0.1:8000/students/{student_id}"


def fetch_data():
    try:
        response = requests.get(GET_STUDENTS_URL)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to fetch data. Status code: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None


def delete_student():
    try:
        response = requests.delete(DELETE_STUDENT_URL)
        if response.status_code == 200:
            return f"Student with student_id '{student_id}' deleted successfully!"
        else:
            st.error(
                f"Failed to delete the student. Status code: {response.status_code}"
            )
            return None
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None


def main():
    st.title("Student Management System")

    get_students = st.button("Get Students List")
    if get_students:
        # Fetch students data from the DB
        data = fetch_data()

        if data:
            st.write("Data fetched successfully:")
            st.write(data)
        else:
            st.write("Failed to fetch data.")

    del_student = st.button("Delete Student")
    if del_student:
        s_id = st.text_input("Pls provide the student_id:")

        if s_id:
            # Delete student from the DB
            data = delete_student()

            if data:
                st.write(data)
            else:
                st.write("Failed to delete the student.")


if __name__ == "__main__":
    main()
