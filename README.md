### Task 1: Comparison of Randomized and Deterministic QuickSort

Implement both randomized and deterministic versions of the QuickSort algorithm. Perform a comparative analysis of their performance by measuring the average execution time on arrays of different sizes.

### Technical Requirements

1. For the implementation of the randomized QuickSort algorithm, create a function `randomized_quick_sort(arr)`, where the pivot element is chosen randomly.

2. For the implementation of the deterministic QuickSort algorithm, create a function `deterministic_quick_sort(arr)`, where the pivot element is chosen using a fixed rule: first, last, or middle element.

3. Create a set of test arrays with different sizes: 10,000, 50,000, 100,000, and 500,000 elements. Fill the arrays with random integers.

4. Measure the execution time of both algorithms on each array. For more accurate results, repeat the sorting of each array 5 times and calculate the average execution time.


### Task 2: Creating a Schedule Using a Greedy Algorithm

Implement a program to create a university class schedule using a greedy algorithm for the set cover problem. The goal is to assign teachers to subjects in such a way that minimizes the number of teachers while covering all subjects.

### Technical Requirements

You are given a set of subjects:  
`{'Mathematics', 'Physics', 'Chemistry', 'Informatics', 'Biology'}`

A list of teachers:

1. **Oleksandr Ivanenko**, 45 years old, o.ivanenko@example.com, subjects: `{'Mathematics', 'Physics'}`
2. **Maria Petrenko**, 38 years old, m.petrenko@example.com, subjects: `{'Chemistry'}`
3. **Serhiy Kovalenko**, 50 years old, s.kovalenko@example.com, subjects: `{'Informatics', 'Mathematics'}`
4. **Nataliya Shevchenko**, 29 years old, n.shevchenko@example.com, subjects: `{'Biology', 'Chemistry'}`
5. **Dmytro Bondarenko**, 35 years old, d.bondarenko@example.com, subjects: `{'Physics', 'Informatics'}`
6. **Olena Hrytsenko**, 42 years old, o.grytsenko@example.com, subjects: `{'Biology'}`

### Task Description

1. Implement the `Teacher` class with the following attributes:
   - `first_name`: (first name)
   - `last_name`: (last name)
   - `age`: (age)
   - `email`: (email address)
   - `can_teach_subjects`: (set of subjects they can teach)

2. Implement the function `create_schedule(subjects, teachers)`, which uses a greedy algorithm to assign teachers to subjects. The function should return a list of teachers and the subjects assigned to them.

3. During the selection of a teacher at each step, prioritize the teacher who can teach the most subjects that are not yet covered. If there are multiple teachers with the same number of subjects, choose the youngest (in terms of age).