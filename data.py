import pandas as pd

# Data for the Midterm Weeks (1-9)
midterm_data = {
    "Week/Nominal Duration/Outcome": [
        "Midterms (45 hours) Week 1 – 9",
        "Week 1: Class Orientation & Overview",
        "Week 2: Introduction to C++ Programming & OOP",
        "Week 3: Classes and Objects",
        "Week 4: Constructors & Destructors",
        "Week 5: Encapsulation & Abstraction",
        "Week 6: Static Members & Methods",
        "Week 7: Inheritance",
        "Week 8: Polymorphism & Virtual Functions",
        "Week 9: Midterm Exam"
    ],
    "Course Content/Subject Matter/Topic/Objectives": [
        "",
        "- Discuss course goals, vision, mission, and policies.\n- Introduce OOP concepts and benefits in C++ programming.",
        "- Introduction to procedural vs. object-oriented programming.\n- Understand basic syntax and structure of C++ programs.\n- Explain objects, classes, and their roles in OOP.",
        "- Explain the structure of a class and its members (data members and functions).\n- Demonstrate how to create objects and use them in a program.",
        "- Explain the role of constructors and destructors.\n- Understand parameterized constructors and their uses.\n- Introduction to dynamic memory management.",
        "- Explain encapsulation and abstraction principles.\n- Use access specifiers (public, private, protected).",
        "- Understand the concept of static member variables and methods.\n- Learn how to use static data members in class design.",
        "- Explain the concept of inheritance and its advantages in OOP.\n- Learn how to implement single and multiple inheritance in C++.",
        "- Understand polymorphism and how it enables dynamic method binding.\n- Learn to implement virtual functions and overriding methods.",
        "- Review and assess knowledge on OOP principles, constructors, encapsulation, inheritance, and polymorphism."
    ],
    "Teaching & Learning Modalities (Activities/Assessment)": [
        "",
        "- Lecture on course overview and policies.\n- Discussion of course objectives and grading system.",
        "- Lecture and code demonstration on basic C++ syntax.\n- Hands-on practice: writing simple C++ programs.\n- Assignment: simple C++ program using basic I/O.",
        "- Lecture on class structure and object instantiation.\n- In-class exercise: Create simple classes and objects.\n- Quiz on classes and basic program structure.",
        "- Lecture on constructors, destructors, and memory management.\n- Lab activity: Write programs implementing parameterized constructors and destructors.",
        "- Code examples: Demonstrate encapsulation in C++ classes.\n- Group activity: Design classes demonstrating encapsulation.",
        "- Lecture on static members.\n- Lab activity: Write programs using static variables and methods.",
        "- Lecture and examples of inheritance in C++.\n- In-class programming activity: Implement simple inheritance.",
        "- Lecture on polymorphism and dynamic binding.\n- Lab: Implement virtual functions and method overriding.",
        "- Midterm exam: Written and practical coding exam covering weeks 1–8 topics."
    ]
}

# Data for the Final Weeks (10-18)
final_data = {
    "Week/Nominal Duration/Outcome": [
        "Finals (45 hours) Week 10 – 18",
        "Week 10: Operator Overloading",
        "Week 11: Friend Functions & Classes",
        "Week 12: Templates",
        "Week 13: Exception Handling",
        "Week 14: File Handling in C++",
        "Week 15: Advanced Topics in OOP",
        "Week 16: Project Development",
        "Week 17: Project Presentation",
        "Week 18: Final Exam"
    ],
    "Course Content/Subject Matter/Topic/Objectives": [
        "",
        "- Understand operator overloading and its use in C++.\n- Learn how to overload various operators such as +, -, <<, and >>.",
        "- Explain the concept of friend functions and classes.\n- Understand how to use friend functions for class access.",
        "- Understand the concept of templates and generic programming.\n- Learn how to implement function and class templates.",
        "- Understand the need for error handling in programs.\n- Learn how to implement exception handling using try, catch, and throw.",
        "- Learn how to read from and write to files using file streams.\n- Understand file handling functions (ifstream, ofstream, etc.).",
        "- Explore advanced OOP topics such as multiple inheritance, virtual inheritance, and abstract classes.",
        "- Apply learned OOP concepts to a practical project.\n- Focus on class design, object management, and implementing real-world solutions using C++.",
        "- Present and demonstrate the final project.\n- Assess the application of OOP concepts in the project.",
        "- Final exam covering all topics from weeks 10–17."
    ],
    "Teaching & Learning Modalities (Activities/Assessment)": [
        "",
        "- Lecture and code examples on operator overloading.\n- Hands-on activity: Implement operator overloading in C++.",
        "- Lecture on friend functions and friend classes.\n- Lab: Write C++ programs using friend functions.",
        "- Lecture and demo on templates.\n- Programming activity: Implement template functions and classes.",
        "- Lecture and demo on exception handling.\n- In-class exercise: Implement basic exception handling in programs.",
        "- Lecture on file handling.\n- Lab: Write programs that implement file I/O operations.",
        "- Lecture and code examples on advanced OOP concepts.\n- Group discussion: Design a system utilizing multiple inheritance.",
        "- Project proposal: Students submit project ideas.\n- In-class project development and consultation.",
        "- Group presentation of projects.\n- Peer evaluation and feedback.",
        "- Written and practical final exam."
    ]
}

# Creating dataframes for both midterm and final
df_midterm = pd.DataFrame(midterm_data)
df_final = pd.DataFrame(final_data)

# Saving both tables to Excel file
with pd.ExcelWriter('/mnt/data/OOP_C++_Syllabus.xlsx') as writer:
    df_midterm.to_excel(writer, sheet_name='Midterms', index=False)
    df_final.to_excel(writer, sheet_name='Finals', index=False)

"/mnt/data/OOP_C++_Syllabus.xlsx"
