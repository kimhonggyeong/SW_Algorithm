
import random

class Student_score_array:

    ####################### 학생 정보 생성 #######################
    def student(self):
        student_dic_list = []
        for _ in range(30): # 30명 이름,나이(18~22),성적(0~100) 랜덤 생성
            name = chr(random.randint(65, 90)) + chr(random.randint(65, 90)) #ASCII 코드 (65~90)로 영어 대문자 생성
            age = random.randint(18, 22) # 나이 생성
            score = random.randint(0, 100) # 성적 생성
            student_dic_list.append({'이름': name, '나이': age, '성적': score}) #학생 리스트에 추가
        return student_dic_list
    
    ####################### 선택정렬 #######################
    def selection_sort(self,A,key,ascending=True):
        n = len(A)
        for i in range(0,n-1,1):
            least = i
            for j in range(i + 1, n):
                if (ascending and A[j][key] < A[least][key]) or (not ascending and A[j][key] > A[least][key]):
                    least = j
            A[i],A[least] = A[least],A[i]

            #print(f"Step {i + 1}: ", [item[key] for item in A])
            #print()
    
    ####################### 삽입정렬 #######################
    def insertion_sort(self, A, key, ascending=True):
        n = len(A)
        for i in range(1,n,1):
            key_item = A[i]
            j = i - 1
            while j>= 0 and ((ascending and A[j][key] > key_item[key]) or (not ascending and A[j][key] < key_item[key])): #key 보다 작은 A[j]가 나올 때 까지
                A[j+1] = A[j]
                j-=1
            A[j+1] = key_item

            #print(f"Step {i + 1}: ", [item[key] for item in A])
            #print()
            

    ####################### 퀵 정렬 (median-of-three 기법을 사용) #######################

    # median-of-three 기법을 사용하여 퀵 정렬의 피벗을 리스트의 첫 번째, 중간, 마지막 요소 중 중간값으로 선택
    def median_of_three(self,A, left, right, key):
        mid = (left + right) // 2
        # 세 값 중 중간값을 선택하기 위해 위치를 정렬
        if A[left][key] > A[mid][key]:
            A[left], A[mid] = A[mid], A[left]  # A[left]는 세 값 중 가장 작은 값
        if A[left][key] > A[right][key]:
            A[left], A[right] = A[right], A[left]  # A[right]가 가장 큰 값이 되고, A[left]는 여전히 최소값
        if A[mid][key] > A[right][key]:
            A[mid], A[right] = A[right], A[mid]  # A[mid]가 A[right] 이하가 되도록
        # 중간값으로 선택한 피벗을 리스트의 첫 번째 위치로 이동
        A[left], A[mid] = A[mid], A[left]
        return A[left]  # 피벗 값 반환

    def quick_sort(self, A, left, right, key, ascending=True):
        if left < right:
            pivot = self.median_of_three(A, left, right, key)
            q = self.partition(A, left, right, pivot, key, ascending)  # 좌우로 분할
            self.quick_sort(A, left, q - 1, key, ascending)  # 왼쪽 부분 리스트 퀵 정렬
            self.quick_sort(A, q + 1, right, key, ascending)  # 오른쪽 부분 리스트 퀵 정렬

    def partition(self,A, left, right, pivot, key, ascending=True):

        low = left + 1
        high = right

        while low <= high:
            # 피벗보다 큰 요소를 찾음
            while low <= right and ((ascending and A[low][key] <= pivot[key]) or (not ascending and A[low][key] >= pivot[key])):
                low += 1


            # 피벗보다 작은 요소를 찾음
            while high >= left and ((ascending and A[high][key] > pivot[key]) or (not ascending and A[high][key] < pivot[key])):
                high -= 1


            # 요소를 교환
            if low < high:
                A[low], A[high] = A[high], A[low]


        # 피벗 교환
        A[left], A[high] = A[high], A[left]


        return high

    ####################### 기수정렬(계수 정렬 알고리즘과 함께 구현) #######################
    def radix_sort(self, A, key,ascending=True):
        Buckets = 10  # 0-9의 십진수
        Digits = 3  # 정렬할 숫자의 최대 자릿수 (필요에 따라 변경 가능)

        factor = 1  # 1의 자리부터 시작

        for d in range(Digits):
            # 1. 계수 정렬용 count 배열 생성 및 초기화
            count = [0] * Buckets
            output = [None] * len(A)

            # 2. 각 자릿수 값의 빈도를 계산
            for student in A:
                digit = (student[key] // factor) % Buckets
                count[digit] += 1

            # 3. count 배열을 누적합으로 변환
            for i in range(1, Buckets):
                count[i] += count[i - 1]

            # 4. 원래 배열을 역순으로 탐색하며 정렬된 결과를 output에 저장
            for student in reversed(A):
                digit = (student[key] // factor) % Buckets
                count[digit] -= 1
                output[count[digit]] = student

            # 5. output 배열을 다시 A로 복사
            for i in range(len(A)):
                A[i] = output[i]

            # 6. 다음 자릿수로 이동
            factor *= Buckets
        
        if not ascending:  # 내림차순일 경우 결과 반전
            A.reverse()

    def main(self):
        choice_list = ['이름','나이','성적'] # 정렬 기준 리스트
        choice_sort_list = ['선택 정렬','삽입 정렬','퀵 정렬','기수 정렬'] # 정렬 방법 리스트
        original_student_list = self.student() # 오리지널 학생 리스트 생성
        
        # 파일로 저장
        with open("student_list_data.txt", "w", encoding="utf-8") as file: 
            for item in original_student_list:
                file.write(f"{item}\n")  # 각 요소를 문자열로 변환하여 한 줄씩 저장

        #생성된 학생정보 출력
        print("\n=== 생성된 학생정보 ===")
        for student in original_student_list:
            print(f"이름: {student['이름']}, 나이: {student['나이']}, 성적: {student['성적']}")

        while True: 
            student_list = [] # 정렬에 사용할 학생 리스트
            #저장된 오리지널 학생 리스트 가져오기
            with open("student_list_data.txt", "r", encoding="utf-8") as file:
                for line in file:
                    student_list.append(eval(line.strip()))

            #정렬 기준 선택
            print("\n=== 학생 성적 관리 시스템 ===")
            print("1. 이름을 기준으로 정렬")
            print("2. 나이를 기준으로 정렬")
            print("3. 성적을 기준으로 정렬")
            print("4. 프로그램 종료")

            choice = input("정렬 기준을 선택하세요: ")

            if choice not in {'1', '2', '3', '4'}:
                print("잘못된 입력입니다. 목록에 있는 숫자를 입력해주세요.")
                continue

             #프로그램 종료가 아닐 시 정렬 방법 선택
            if choice != '4':
                print("\n1. 선택 정렬")
                print("2. 삽입 정렬")
                print("3. 퀵 정렬")
                if choice == '3':  # 성적 기준 정렬 시 기수 정렬 추가
                    print("4. 기수 정렬")

                choice_sort = input("정렬 알고리즘 선택: ")

                valid_sort_choices = {'1', '2', '3'} # 정렬 알고리즘 번호 리스트
                if choice == '3':  # 성적 정렬에서만 '4' 추가
                    valid_sort_choices.add('4')
            
                if choice_sort not in valid_sort_choices: # 선택한 정렬 알고리즘이 valid_sort_choices 리스트에 존재 하는지 확인
                    print("잘못된 입력입니다. 목록에 있는 숫자를 입력해주세요.")
                    continue
            
                # 정렬 방향 선택
                print("\n1. 오름차순")
                print("2. 내림차순")
                ascending = input("정렬 방향을 선택하세요: ")
                if ascending not in {'1', '2'}:
                    print("잘못된 입력입니다. 오름차순(1) 또는 내림차순(2)을 선택해주세요.")
                    continue

                ascending = ascending == '1'  # 오름차순 여부 결정

            elif choice == '4':  # 종료 조건
                print("프로그램을 종료합니다.")
                return

            # 선택한것 확인
            print(
            f"{choice_list[int(choice) - 1]}을 기준으로 "
            f"{choice_sort_list[int(choice_sort) - 1]} 방식으로 "
            f"{'오름차순' if ascending else '내림차순'} 정렬합니다."
        )
            
            # 선택한 알고리즘에 따라 실행
            if choice_sort == '1':
                self.selection_sort(student_list, choice_list[int(choice)-1], ascending)
            elif choice_sort == '2':
                self.insertion_sort(student_list, choice_list[int(choice)-1], ascending)
            elif choice_sort == '3':
                self.quick_sort(student_list, 0, len(student_list) - 1, choice_list[int(choice) - 1], ascending)
            elif choice_sort == '4':
                self.radix_sort(student_list, choice_list[int(choice)-1], ascending)
            print()
            print("정렬 후:") # 결과 출력
            for student in student_list:
                print(f"이름: {student['이름']}, 나이: {student['나이']}, 성적: {student['성적']}")


if __name__ == "__main__":
    Student_score_array().main()
