import pandas as pd
import json
dataset = []

#Role-1 : Data Analyst
dataset.append({
    "job_role": "data analyst",
    "core_skills": "sql, excel, python, data analysis, pandas, statistics, power bi",
    "optional_skills": "tableau, r, communication, data visualization",
    "skill_resources": json.dumps({
        "sql": {
            "free": "[Khan Academy – SQL](https://www.khanacademy.org/computing/computer-programming/sql)",
            "paid": "[Udemy – SQL Bootcamp](https://www.udemy.com/course/the-complete-sql-bootcamp/)"
        },
        "excel": {
            "free": "[Excel Easy](https://www.excel-easy.com/)",
            "paid": "[Coursera – Google Data Analytics](https://www.coursera.org/professional-certificates/google-data-analytics)"
        },
        "python": {
            "free": "[freeCodeCamp – Python](https://www.freecodecamp.org/learn/)",
            "paid": "[Udemy – Python Mega Course](https://www.udemy.com/course/the-python-mega-course/)"
        },
        "data analysis": {
            "free": "[Kaggle Learn – Data Analysis](https://www.kaggle.com/learn/pandas)",
            "paid": "[Coursera – Data Analysis with Python](https://www.coursera.org/learn/data-analysis-with-python)"
        },
        "pandas": {
            "free": "[Pandas Docs](https://pandas.pydata.org/docs/)",
            "paid": "[Udemy – Pandas](https://www.udemy.com/course/data-analysis-with-pandas/)"
        },
        "statistics": {
            "free": "[Khan Academy – Statistics](https://www.khanacademy.org/math/statistics-probability)",
            "paid": "[Coursera – Stanford Statistics](https://www.coursera.org/learn/stanford-statistics)"
        },
        "power bi": {
            "free": "[Microsoft](https://learn.microsoft.com/en-us/training/powerplatform/power-bi)",
            "paid": "[Linkedin Learning](https://www.linkedin.com/learning/power-bi-essential-training)"
        }
    })
})

# Role 2: Frontend Developer
dataset.append({
    "job_role": "frontend developer",
    "core_skills": "html, css, javascript, react, typescript",
    "optional_skills": "redux, vue.js, angular, ui/ux, figma",
    "skill_resources": json.dumps({
        "html": {
            "free": "[MDN – HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)",
            "paid": "[Coursera – Meta Frontend](https://www.coursera.org/professional-certificates/meta-front-end-developer)"
        },
        "css": {
            "free": "[MDN – CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)",
            "paid": "[Udemy – Web Developer Bootcamp](https://www.udemy.com/course/the-web-developer-bootcamp/)"
        },
        "javascript": {
            "free": "[freeCodeCamp – JS](https://www.freecodecamp.org/learn/)",
            "paid": "[Frontend Masters – JavaScript](https://frontendmasters.com/courses/javascript-basics/)"
        },
        "react": {
            "free": "[React Docs](https://react.dev/learn)",
            "paid": "[Udemy – React Complete Guide](https://www.udemy.com/course/react-the-complete-guide-incl-redux/)"
        },
        "typescript": {
            "free": "[TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)",
            "paid": "[Udemy – TS for React Devs](https://www.udemy.com/course/understanding-typescript/)"
        }
    })
})

# Role 3: UI/UX Designer
dataset.append({
    "job_role": "ui/ux designer",
    "core_skills": "ui/ux, wireframing, figma, adobe xd, prototyping",
    "optional_skills": "sketch, photoshop, html, css, creativity",
    "skill_resources": json.dumps({
        "ui/ux": {
            "free": "[Foundations of User Experience (UX) Design – Coursera](https://www.coursera.org/learn/foundations-user-experience-design)",
            "paid": "[Figma + Adobe XD Master Course – Udemy](https://www.udemy.com/course/figma-adobe-xd-bootcamp-learn-uiux-design-az/)"
    },
        "wireframing": {
            "free": "[Figma – Wireframe Basics](https://help.figma.com/hc/en-us/articles/360040451373-Design-a-wireframe)",
            "paid": "[UI/UX Design Masterclass with Adobe XD – Udemy](https://www.udemy.com/course/uiux-design-masterclass-with-adobe-xd-from-beginner-to-pro/)"
    },
        "figma": {
            "free": "[Figma Learn – Official Guide](https://help.figma.com/hc/en-us)",
            "paid": "[UI/UX Design Essentials Bootcamp with Figma – Udemy](https://www.udemy.com/course/uiux-design-bootcamp-with-figma/)"
    },
        "adobe xd": {
            "free": "[Adobe XD Tutorials – Adobe](https://helpx.adobe.com/xd/tutorials.html)",
            "paid": "[Essentials User Experience Design – Adobe XD – Udemy](https://www.udemy.com/course/essentials-user-experience-design-adobe-xd-ui-ux-design/)"
    },
        "prototyping": {
            "free": "[Figma – Prototyping Basics](https://help.figma.com/hc/en-us/articles/360040529373-Create-interactive-prototypes)",
            "paid": "[Figma 2025 – UX/UI Design Bootcamp – Udemy](https://www.udemy.com/course/figma-2025-ux-design-bootcamp/)"
        }
    })
})

# Role 4: Digital Marketer
dataset.append({
    "job_role": "digital marketer",
    "core_skills": "digital marketing, seo, google analytics, content creation, social media",
    "optional_skills": "ppc, marketing campaigns, wordpress, analytics",
    "skill_resources": json.dumps({
        "digital marketing": {
            "free": "[Google Digital Garage](https://learndigital.withgoogle.com/digitalgarage)",
            "paid": "[Coursera – Digital Marketing](https://www.coursera.org/specializations/digital-marketing)"
        },
        "seo": {
            "free": "[Yoast – SEO Basics](https://yoast.com/academy/free-seo-training-seo-for-beginners/)",
            "paid": "[Udemy – SEO Mastery](https://www.udemy.com/course/ultimate-seo-training-course/?srsltid=AfmBOorjkK6ExyXO9B13MlWDfpB7fl9sev-PZUVVN7uBoHSeY7qrjmNT)"
        },
        "google analytics": {
            "free": "[Google Analytics Academy](https://analytics.google.com/analytics/academy/)",
            "paid": "[Udemy – GA](https://www.udemy.com/course/advanced-google-analytics-course-77-practical-questions/)"
        },
        "content creation": {
            "free": "[HubSpot Content Course](https://academy.hubspot.com/courses/content-marketing)",
            "paid": "[LinkedIn – Content Marketing](https://www.udemy.com/course/complete-content-marketing-masterclass-content-that-sells/)"
        },
        "social media": {
            "free": "[Meta Blueprint](https://www.facebook.com/business/learn)",
            "paid": "[Coursera – Social Media Marketing](https://www.coursera.org/specializations/social-media-marketing)"
        }
    })
})

# Role 5: Human Resources Executive
dataset.append({
    "job_role": "human resources executive",
    "core_skills": "hr management, recruitment, hr policies, communication, leadership",
    "optional_skills": "stakeholder management, project management, employee relations",
    "skill_resources": json.dumps({
        "hr management": {
            "free": "[Alison – HR Management](https://alison.com/course/diploma-in-human-resources-hr)",
            "paid": "[Coursera – Human Resource Management](https://www.coursera.org/specializations/human-resource-management)"
        },
        "recruitment": {
            "free": "[LinkedIn – Recruiting](https://www.linkedin.com/learning/recruiting-foundations)",
            "paid": "[Udemy – Recruitment Skills](https://www.udemy.com/course/ultimate-recruitment-talentacquisition/)"
        },
        "hr policies": {
            "free": "[HR University Blog](https://www.humanresourcedegree.org/)",
            "paid": "[Udemy – HR Policy](https://www.udemy.com/course/hr-leadership/)"
        },
        "communication": {
            "free": "[Cursa – Communication](https://cursa.app/en/free-course/human-resource-management-chhj)",
            "paid": "[Udemy – Communication Skills](https://www.udemy.com/course/hr-leadership/)"
        },
        "leadership": {
            "free": "[Coursera – Leading Teams](https://www.coursera.org/learn/leading-teams)",
            "paid": "[Shiksha – Leadership Skills](https://www.shiksha.com/online-courses/crash-course-on-leadership-skills-development-negotiation-course-udeml1041)"
        }
    })
})

# Role 6: Full Stack Developer
dataset.append({
    "job_role": "full stack developer",
    "core_skills": "html, css, javascript, react, node.js, express, mongodb",
    "optional_skills": "typescript, redux, mysql, docker, git",
    "skill_resources": json.dumps({
        "html": {
            "free": "[MDN – HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)",
            "paid": "[Coursera – Meta Frontend](https://www.coursera.org/professional-certificates/meta-front-end-developer)"
        },
        "css": {
            "free": "[MDN – CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)",
            "paid": "[Udemy – Web Developer Bootcamp](https://www.udemy.com/course/the-web-developer-bootcamp/)"
        },
        "javascript": {
            "free": "[freeCodeCamp – JS](https://www.freecodecamp.org/learn/)",
            "paid": "[Frontend Masters – JavaScript](https://frontendmasters.com/courses/javascript-basics/)"
        },
        "react": {
            "free": "[React Docs](https://react.dev/learn)",
            "paid": "[Udemy – React Guide](https://www.udemy.com/course/react-the-complete-guide-incl-redux/)"
        },
        "node.js": {
            "free": "[Node.js Docs](https://nodejs.org/en/docs)",
            "paid": "[Udemy – Node.js Bootcamp](https://www.udemy.com/course/the-complete-nodejs-developer-course/)"
        },
        "express": {
            "free": "[MDN – Express Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs)",
            "paid": "[Udemy – Node/Express Course](https://www.udemy.com/course/nodejs-express-mongodb-bootcamp/)"
        },
        "mongodb": {
            "free": "[MongoDB University](https://university.mongodb.com/)",
            "paid": "[Udemy – MongoDB for Beginners](https://www.udemy.com/course/mongodb-the-complete-developers-guide/)"
        }
    })
})

# Role 7: DevOps Engineer
dataset.append({
    "job_role": "devops engineer",
    "core_skills": "linux, docker, kubernetes, jenkins, ci/cd",
    "optional_skills": "terraform, aws, ansible, python, git",
    "skill_resources": json.dumps({
        "linux": {
            "free": "[Linux Journey](https://linuxjourney.com/)",
            "paid": "[Udemy – Linux Mastery](https://www.udemy.com/course/linux-mastery/)"
        },
        "docker": {
            "free": "[Docker Docs](https://docs.docker.com/)",
            "paid": "[Udemy – Docker Mastery](https://www.udemy.com/course/docker-mastery/)"
        },
        "kubernetes": {
            "free": "[Kubernetes Docs](https://kubernetes.io/docs/home/)",
            "paid": "[Udemy – Kubernetes for DevOps](https://www.udemy.com/course/docker-kubernetes-the-practical-guide/)"
        },
        "jenkins": {
            "free": "[Jenkins Tutorials](https://www.jenkins.io/doc/)",
            "paid": "[LinkedIn Learning – Jenkins CI/CD](https://www.linkedin.com/learning/jenkins-essential-training)"
        },
        "ci/cd": {
            "free": "[GitHub Actions Docs](https://docs.github.com/en/actions)",
            "paid": "[Coursera – CI/CD Pipelines](https://www.udemy.com/course/gitlab-ci-pipelines-cicd-and-devops-for-beginners/)"
        }
    })
})

# Role 8: Database Administrator
dataset.append({
    "job_role": "database administrator",
    "core_skills": "sql, mysql, postgresql, database design, sql server",
    "optional_skills": "mongodb, backup and recovery, linux, performance tuning",
    "skill_resources": json.dumps({
        "sql": {
            "free": "[SQL Tutorial – W3Schools](https://www.w3schools.com/sql/)",
            "paid": "[Udemy – SQL Bootcamp](https://www.udemy.com/course/the-complete-sql-bootcamp/)"
        },
        "mysql": {
            "free": "[MySQL Docs](https://dev.mysql.com/doc/)",
            "paid": "[Coursera – SQL for Data Science](https://www.coursera.org/learn/sql-for-data-science)"
        },
        "postgresql": {
            "free": "[PostgreSQL Tutorial](https://www.postgresqltutorial.com/)",
            "paid": "[Udemy – PostgreSQL Bootcamp](https://www.udemy.com/course/sql-and-postgresql-for-beginners/)"
        },
        "database design": {
            "free": "[Vertabelo Blog](https://www.vertabelo.com/blog/)",
            "paid": "[Coursera – Database Design](https://www.coursera.org/learn/database-management)"
        },
        "sql server": {
            "free": "[Microsoft Docs – SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/)",
            "paid": "[Datacamp – SQL](https://www.datacamp.com/tracks/sql-for-database-administrators)"
        }
    })
})

# Role 9: Mobile Developer
dataset.append({
    "job_role": "mobile developer",
    "core_skills": "android development, java, kotlin, ios development, swift",
    "optional_skills": "flutter, react native, firebase, ui/ux design",
    "skill_resources": json.dumps({
        "android development": {
            "free": "[Android Developers](https://developer.android.com/courses)",
            "paid": "[Android Development](https://hyperskill.org/courses/16))"
        },
        "java": {
            "free": "[Java – W3Schools](https://www.w3schools.com/java/)",
            "paid": "[Coursera – Java Programming](https://www.coursera.org/specializations/java-programming)"
        },
        "kotlin": {
            "free": "[Kotlin Docs](https://kotlinlang.org/docs/home.html)",
            "paid": "[Udemy – Kotlin Android Dev](https://www.udemy.com/course/kotlin-android-developer-masterclass/)"
        },
        "ios development": {
            "free": "[Apple Developer – iOS](https://developer.apple.com/ios/)",
            "paid": "[Udemy – iOS Dev with Swift](https://www.udemy.com/course/ios-13-app-development-bootcamp/)"
        },
        "swift": {
            "free": "[Swift.org](https://www.swift.org/documentation/)",
            "paid": "[Udemy – iOS App Dev](https://www.udemy.com/course/swiftui-masterclass-course-ios-development-with-swift/)"
        }
    })
})

# Role 10: Software Architect
dataset.append({
    "job_role": "software architect",
    "core_skills": "software design, system architecture, microservices, spring boot, leadership",
    "optional_skills": "aws, docker, agile, database design, api design",
    "skill_resources": json.dumps({
        "software design": {
            "free": "[Refactoring Guru](https://refactoring.guru/design-patterns)",
            "paid": "[Fundamentals of Software Design](https://www.udemy.com/course/fundamentals-of-software-design-and-software-architecture-course/)"
        },
        "system architecture": {
            "free": "[MIT - OpenCourseWare]https://ocw.mit.edu/courses/16-842-fundamentals-of-systems-engineering-fall-2015/)",
            "paid": "[Udemy – System Design](https://www.udemy.com/course/system-design-bootcamp/)"
        },
        "microservices": {
            "free": "[Microservices.io](https://microservices.io/)",
            "paid": "[Udemy – Microservices w/ Spring](https://www.udemy.com/course/microservices-with-spring-boot/)"
        },
        "spring boot": {
            "free": "[Spring Boot Docs](https://spring.io/projects/spring-boot)",
            "paid": "[Udemy – Spring Boot Masterclass](https://www.udemy.com/course/spring-boot-tutorial-for-beginners/)"
        },
        "leadership": {
            "free": "[MindTools – Leadership](https://www.mindtools.com/pages/main/newMN_LDR.htm)",
            "paid": "[Coursera – Leadership](https://www.coursera.org/learn/leading-teams)"
        }
    })
})

# Role 11: Cybersecurity Analyst
dataset.append({
    "job_role": "cyber security analyst",
    "core_skills": "network security, firewalls, ethical hacking, siem, penetration testing",
    "optional_skills": "linux, python, cybersecurity tools, risk analysis",
    "skill_resources": json.dumps({
        "network security": {
            "free": "[Great Learning – Network Security](https://www.mygreatlearning.com/academy/learn-for-free/courses/network-security)",
            "paid": "[Udemy – Network Security](https://www.udemy.com/course/network-security-course/)"
        },
        "firewalls": {
            "free": "[Wikipedia](https://en.wikipedia.org/wiki/National_Initiative_for_Cybersecurity_Careers_and_Studies)",
            "paid": "[Udemy – Firewalls](https://www.udemy.com/course/palo-alto-firewall-mastery-complete-training-2025/)"
        },
        "ethical hacking": {
            "free": "[Great Learning](https://www.mygreatlearning.com/academy/learn-for-free/courses/network-security)",
            "paid": "[Udemy – CEH Ethical Hacking](https://www.udemy.com/course/learn-ethical-hacking-from-scratch/)"
        },
        "siem": {
            "free": "[IBM QRadar SIEM](https://www.ibm.com/docs/en/qradar-common?topic=learning-qradar-tutorials)",
            "paid": "[Coursera – Security Analyst](https://www.coursera.org/specializations/ibm-cybersecurity-analyst)"
        },
        "penetration testing": {
            "free": "[TryHackMe – Pentesting](https://tryhackme.com/)",
            "paid": "[Udemy – Pentesting](https://www.udemy.com/course/penetration-testing/)"
        }
    })
})

# Role 12: Business Analyst
dataset.append({
    "job_role": "business analyst",
    "core_skills": "excel, sql, data visualization, communication, problem solving",
    "optional_skills": "power bi, stakeholder management, tableau, statistics",
    "skill_resources": json.dumps({
        "excel": {
            "free": "[Excel Easy](https://www.excel-easy.com/)",
            "paid": "[Coursera – Excel Skills for Business](https://www.coursera.org/specializations/excel)"
        },
        "sql": {
            "free": "[Khan Academy – SQL](https://www.khanacademy.org/computing/computer-programming/sql)",
            "paid": "[Udemy – SQL Bootcamp](https://www.udemy.com/course/the-complete-sql-bootcamp/)"
        },
        "data visualization": {
            "free": "[Kaggle – Data Visualization](https://www.kaggle.com/learn/data-visualization)",
            "paid": "[Udemy – Data Viz with Tableau](https://www.udemy.com/course/tableau10/)"
        },
        "communication": {
            "free": "[Coursera – Communication Skills](https://www.coursera.org/learn/wharton-communication-skills)",
            "paid": "[Udemy – Business Communication](https://www.udemy.com/course/effective-business-communication-a/)"
        },
        "problem solving": {
            "free": "[Alison – Problem Solving](https://alison.com/course/problem-solving-and-critical-thinking-skills)",
            "paid": "[Coursera – Critical Thinking](https://www.coursera.org/learn/critical-thinking-skills)"
        }
    })
})

# Role 13: Game Developer
dataset.append({
    "job_role": "game developer",
    "core_skills": "unity, c#, game design, game physics, creativity",
    "optional_skills": "unreal engine, 3d modeling, vr development, blender",
    "skill_resources": json.dumps({
        "unity": {
            "free": "[Unity Learn](https://learn.unity.com/)",
            "paid": "[Udemy – Unity Game Dev](https://www.udemy.com/course/unitycourse/)"
        },
        "c#": {
            "free": "[C# – Microsoft Docs](https://learn.microsoft.com/en-us/dotnet/csharp/)",
            "paid": "[Unity Learn - C#](https://learn.unity.com/pathway/junior-programmer)"
        },
        "game design": {
            "free": "[Coursera - Game Design](https://www.coursera.org/learn/game-design)",
            "paid": "[Coursera – Game Design](https://www.coursera.org/learn/game-design)"
        },
        "game physics": {
            "free": "[Gamasutra Physics Basics](https://www.gamedeveloper.com/programming/physics-in-games-101)",
            "paid": "[Udemy – Physics](https://www.udemy.com/topic/game-physics/)"
        },
        "creativity": {
            "free": "[IDEO – Design Thinking](https://www.ideou.com/pages/design-thinking)",
            "paid": "[LinkedIn – Creativity Boost](https://www.linkedin.com/learning/creativity-for-all)"
        }
    })
})

# Role 14: Blockchain Developer
dataset.append({
    "job_role": "blockchain developer",
    "core_skills": "blockchain, solidity, smart contracts, ethereum, web3",
    "optional_skills": "web3js, node.js, cryptography, truffle",
    "skill_resources": json.dumps({
        "blockchain": {
            "free": "[Coursera - Blockhain basics](https://www.coursera.org/learn/blockchain-basics)",
            "paid": "[Coursera - BlockchainSpecialization(https://www.coursera.org/specializations/blockchain)"
        },
        "solidity": {
            "free": "[Solidity Docs](https://docs.soliditylang.org/en/latest/)",
            "paid": "[Udemy – Solidity Dev Bootcamp](https://www.udemy.com/course/ethereum-and-solidity-the-complete-developers-guide/)"
        },
        "smart contracts": {
            "free": "[Ethereum Smart Contract Basics](https://ethereum.org/en/developers/docs/smart-contracts/)",
            "paid": "[Udemy – Developers Guide](https://www.udemy.com/course/ethereum-and-solidity-the-complete-developers-guide/)"
        },
        "ethereum": {
            "free": "[Ethereum Dev Portal](https://ethereum.org/en/developers/)",
            "paid": "[Udemy – Ethereum Developer](https://www.udemy.com/course/ethereum-and-solidity-the-complete-developers-guide/)"
        },
        "web3": {
            "free": "[Alchemy Web3 Guide](https://www.alchemy.com/university)",
            "paid": "[Alchemy](https://www.alchemy.com/overviews/solidity-bootcamp)"
        }
    })
})

# Role 15: Artificial Intelligence Engineer
dataset.append({
    "job_role": "artificial intelligence engineer",
    "core_skills": "python, machine learning, deep learning, tensorflow, keras",
    "optional_skills": "pandas, nlp, statistics, data science",
    "skill_resources": json.dumps({
        "python": {
            "free": "[freeCodeCamp – Python](https://www.freecodecamp.org/learn/)",
            "paid": "[Udemy – Python Mega Course](https://www.udemy.com/course/the-python-mega-course/)"
        },
        "machine learning": {
            "free": "[Google ML Crash Course](https://developers.google.com/machine-learning/crash-course)",
            "paid": "[Coursera – Andrew Ng ML](https://www.coursera.org/learn/machine-learning)"
        },
        "deep learning": {
            "free": "[DeepLearning.ai Blog](https://www.deeplearning.ai/)",
            "paid": "[Coursera – Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning)"
        },
        "tensorflow": {
            "free": "[TensorFlow Tutorials](https://www.tensorflow.org/tutorials)",
            "paid": "[Udemy – TF Developer](https://www.udemy.com/course/tensorflow-developer-certificate-machine-learning-zero-to-mastery/)"
        },
        "keras": {
            "free": "[Keras Docs](https://keras.io/guides/)",
            "paid": "[Udemy – Keras Deep Learning](https://www.udemy.com/course/tensorflow-developer-certificate-machine-learning-zero-to-mastery/)"
        }
    })
})

# Role 16: Cloud Engineer
dataset.append({
    "job_role": "cloud engineer",
    "core_skills": "aws, azure, gcp, linux, docker",
    "optional_skills": "terraform, kubernetes, devops, shell scripting, python",
    "skill_resources": json.dumps({
        "aws": {
            "free": "[AWS Skill Builder](https://skillbuilder.aws/)",
            "paid": "[Coursera – AWS Fundamentals](https://www.coursera.org/specializations/aws-fundamentals)"
        },
        "azure": {
            "free": "[Microsoft Learn – Azure](https://learn.microsoft.com/en-us/training/azure/)",
            "paid": "[Linkedin Learning - Azure](https://www.linkedin.com/learning/paths/become-an-azure-administrator/)"
        },
        "gcp": {
            "free": "[Google Cloud Training](https://cloud.google.com/training)",
            "paid": "[Coursera – GCP Associate](https://www.coursera.org/professional-certificates/cloud-engineering-gcp)"
        },
        "linux": {
            "free": "[Linux Journey](https://linuxjourney.com/)",
            "paid": "[Udemy – Linux Mastery](https://www.udemy.com/course/linux-mastery/)"
        },
        "docker": {
            "free": "[Docker Docs](https://docs.docker.com/get-started/)",
            "paid": "[Udemy – Docker Mastery](https://www.udemy.com/course/docker-mastery/)"
        }
    })
})

# Role 17: Systems Analyst
dataset.append({
    "job_role": "systems analyst",
    "core_skills": "system design, requirements analysis, data modeling, communication, problem solving",
    "optional_skills": "sql, er diagrams, project management, testing",
    "skill_resources": json.dumps({
        "system design": {
            "free": "[System Design Primer – GitHub](https://github.com/donnemartin/system-design-primer)",
            "paid": "[Udemy – System Design Interview](https://www.udemy.com/course/grokking-the-system-design-interview/)"
        },
        "requirements analysis": {
            "free": "[Coursera – Requirements Gathering](https://www.coursera.org/learn/requirements-gathering-in-business-analysis)",
            "paid": "[Coursera – Requirements Engineering](https://www.coursera.org/specializations/requirements-engineering-secure-software)"
        },
        "data modeling": {
            "free": "[Udemy – Data Modeling](https://www.udemy.com/course/data-modeling-for-beginners-free-course/)",
            "paid": "[Coursera – Data Modeling](https://www.coursera.org/learn/data-modeling-transformation-serving)"
        },
        "communication": {
            "free": "[Cousera – Business Analysis](https://www.coursera.org/learn/business-analysis-process-modeling-requirements-gathering)",
            "paid": "[The BA Guide](https://thebaguide.com/course_landing_page/understand-and-elicit-requirements/)"
        },
        "problem solving": {
            "free": "[FutureLearn – Problem Solving](https://www.futurelearn.com/courses/problem-solving)",
            "paid": "[Coursera – Critical Thinking](https://www.coursera.org/learn/critical-thinking-skills)"
        }
    })
})

# Role 18: Data Engineer
dataset.append({
    "job_role": "data engineer",
    "core_skills": "python, sql, data pipelines, etl, apache spark",
    "optional_skills": "hadoop, cloud storage, bigquery, airflow",
    "skill_resources": json.dumps({
        "python": {
            "free": "[freeCodeCamp – Python](https://www.freecodecamp.org/learn/)",
            "paid": "[Udemy – Python Bootcamp](https://www.udemy.com/course/complete-python-bootcamp/)"
        },
        "sql": {
            "free": "[Khan Academy – SQL](https://www.khanacademy.org/computing/computer-programming/sql)",
            "paid": "[Udemy – SQL Bootcamp](https://www.udemy.com/course/the-complete-sql-bootcamp/)"
        },
        "data pipelines": {
            "free": "[AWS – Data Pipeline Guide](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/what-is-datapipeline.html)",
            "paid": "[Coursera – Building Data Pipelines](https://www.coursera.org/learn/data-engineering-gcp)"
        },
        "etl": {
            "free": "[Talend Blog – ETL Basics](https://www.talend.com/resources/what-is-etl/)",
            "paid": "[Udemy – ETL](https://www.udemy.com/course/alteryx-masterclass-for-data-analytics-etl-and-reporting/)"
        },
        "apache spark": {
            "free": "[Spark Docs](https://spark.apache.org/docs/latest/)",
            "paid": "[Datacamp – Spark](https://www.datacamp.com/courses/introduction-to-pyspark)"
        }
    })
})

# Role 19: QA/Test Engineer
dataset.append({
    "job_role": "qa/test engineer",
    "core_skills": "manual testing, automation testing, selenium, test cases, bug tracking",
    "optional_skills": "java, jira, api testing, performance testing",
    "skill_resources": json.dumps({
        "manual testing": {
            "free": "[Guru99 – Manual Testing](https://www.guru99.com/manual-testing.html)",
            "paid": "[Udemy – Manual Testing Basics](https://www.udemy.com/course/manual-software-testing-h/)"
        },
        "automation testing": {
            "free": "[Software Testing Help](https://www.softwaretestinghelp.com/automation-testing-tutorial-1/)",
            "paid": "[Udemy – Automation Testing](https://www.udemy.com/course/automation-testing-masterclass/)"
        },
        "selenium": {
            "free": "[Selenium.dev Docs](https://www.selenium.dev/documentation/)",
            "paid": "[Udemy – Selenium WebDriver](https://www.udemy.com/course/selenium-real-time-examplesinterview-questions/)"
        },
        "test cases": {
            "free": "[Guru99 – Test Cases](https://www.guru99.com/test-case.html)",
            "paid": "[Software Testing](https://www.udemy.com/course/test-case/)"
        },
        "bug tracking": {
            "free": "[Atlassian – Jira Bug Tracking](https://www.atlassian.com/software/jira/bug-tracking)",
            "paid": "[Udemy – Jira for Testers](https://www.udemy.com/course/bug-tracking-with-jira-jira-for-softwareqa-testers/)"
        }
    })
})

# Role 20: Product Manager
dataset.append({
    "job_role": "product manager",
    "core_skills": "product strategy, roadmapping, user research, communication, agile",
    "optional_skills": "sql, jira, data analysis, prototyping, ux",
    "skill_resources": json.dumps({
        "product strategy": {
            "free": "[Roman Pichler Blog](https://www.romanpichler.com/blog/)",
            "paid": "[Coursera – Digital Product Management](https://www.coursera.org/learn/uva-darden-digital-product-management)"
        },
        "roadmapping": {
            "free": "[Coursera – Roadmaping](https://www.coursera.org/learn/microsoft-product-strategy-and-roadmapping)",
            "paid": "[ProdPad – Roadmaps](https://www.prodpad.com/downloads/roadmap-course/)"
        },
        "user research": {
            "free": "[uxcel – User Research](https://app.uxcel.com/courses/intro-product-management)",
            "paid": "[LinkedIn – User Research](https://www.linkedin.com/learning/ux-foundations-research)"
        },
        "communication": {
            "free": "[Careerfoundry – Communication](https://careerfoundry.com/en/tutorials/product-management-for-beginners/roadmaps-and-communication)",
            "paid": "[Linkedin Learning – Communication Skills](https://www.linkedin.com/learning/becoming-a-product-manager-a-complete-guide)"
        },
        "agile": {
            "free": "[Agile Alliance Resources](https://www.agilealliance.org/agile101/)",
            "paid": "[Coursera – Agile Development](https://www.coursera.org/specializations/agile-development)"
        }
    })
})

# Role 21: Technical Writer
dataset.append({
    "job_role": "technical writer",
    "core_skills": "technical writing, grammar, documentation, communication, research",
    "optional_skills": "markdown, html, content creation, version control",
    "skill_resources": json.dumps({
        "technical writing": {
            "free": "[Google Tech Writing Course](https://developers.google.com/tech-writing)",
            "paid": "[Coursera – Technical Writing Essentials](https://www.coursera.org/learn/technical-writing-esl)"
    },
        "grammar": {
            "free": "[Grammarly Blog](https://www.grammarly.com/blog/category/handbook/)",
            "paid": "[Udemy – English Grammar Launch: Upgrade Your Speaking](https://www.udemy.com/course/english-grammar-launch-upgrade-your-speaking-and-listening/)"
    },
        "documentation": {
            "free": "[Write the Docs](https://www.writethedocs.org/guide/)",
            "paid": "[LinkedIn Learning – Creating Technical Documentation](https://www.linkedin.com/learning/creating-technical-documentation-2)"
    },
        "communication": {
            "free": "[Coursera – Improving Communication Skills](https://www.coursera.org/learn/wharton-communication-skills)",
            "paid": "[Udemy – Communication Skills for Workplace & Social Success](https://www.udemy.com/course/communication-skills-for-workplace-social-success/)"
    },
        "research": {
            "free": "[MIT OCW – Science Writing & New Media](https://ocw.mit.edu/courses/comparative-media-studies-writing/21w-035-science-writing-and-new-media-spring-2014/)",
            "paid": "[Coursera – Writing a Research Paper](https://www.coursera.org/learn/how-to-write-a-research-paper)"
        }
    })
})

# Role 22: IT Support Specialist
dataset.append({
    "job_role": "it support specialist",
    "core_skills": "networking, troubleshooting, operating systems, customer support, hardware",
    "optional_skills": "linux, security, virtualization, cloud fundamentals",
    "skill_resources": json.dumps({
        "networking": {
            "free": "[Cisco – Networking Basics](https://skillsforall.com/course/networking-basics)",
            "paid": "[Coursera – Google IT Support](https://www.coursera.org/professional-certificates/google-it-support)"
        },
        "troubleshooting": {
            "free": "[CompTIA Resources](https://www.comptia.org/resources)",
            "paid": "[Get Your Education](https://www.getyoureducation.net/course/technical-support-fundamentals)"
        },
        "operating systems": {
            "free": "[Microsoft Learn – Windows](https://learn.microsoft.com/en-us/training/)",
            "paid": "[Coursera - IT Support](https://www.coursera.org/professional-certificates/google-it-support)"
        },
        "customer support": {
            "free": "[Udemy](https://www.udemy.com/course/customer-support-skills/)",
            "paid": "[Coursera – Customer Support](https://www.coursera.org/specializations/customer-service)"
        },
        "hardware": {
            "free": "[Coursera - Hardware Basics](https://www.coursera.org/learn/technical-support-fundamentals)",
            "paid": "[Udemy – Computer Hardware](https://www.udemy.com/course/computer-networking-and-hardware-basics-for-beginners/)"
        }
    })
})

# Role 23: SEO Specialist
dataset.append({
    "job_role": "seo specialist",
    "core_skills": "seo, google analytics, keyword research, content strategy, on-page seo",
    "optional_skills": "sem, ppc, wordpress, technical seo",
    "skill_resources": json.dumps({
        "seo": {
            "free": "[Moz Beginner's Guide](https://moz.com/beginners-guide-to-seo)",
            "paid": "[Udemy – SEO 2025](https://www.udemy.com/course/seo-course-2025-from-beginner-to-advanced-step-by-step/)"
        },
        "google analytics": {
            "free": "[Google Analytics Academy](https://analytics.google.com/analytics/academy/)",
            "paid": "[Google Analytics 2025](https://www.udemy.com/course/google-analytics-complete/)"
        },
        "keyword research": {
            "free": "[Ahrefs Guide](https://ahrefs.com/blog/keyword-research/)",
            "paid": "[SEMRush Academy – Keyword](https://www.semrush.com/academy/courses/keyword-research-course-with-greg-gifford)"
        },
        "content strategy": {
            "free": "[Content Marketing Institute](https://contentmarketinginstitute.com/)",
            "paid": "[LinkedIn – Content Strategy](https://www.linkedin.com/learning/content-marketing-foundations)"
        },
        "on-page seo": {
            "free": "[Backlinko – On-Page SEO](https://backlinko.com/on-page-seo)",
            "paid": "[On-Page SEO Training](https://www.udemy.com/course/on-page-web-optimization-for-seo/)"
        }
    })
})

# Role 24: API Developer
dataset.append({
    "job_role": "api developer",
    "core_skills": "rest apis, json, node.js, express, postman",
    "optional_skills": "swagger, graphql, api security, oauth",
    "skill_resources": json.dumps({
        "rest apis": {
            "free": "[RESTful API Tutorial](https://restfulapi.net/)",
            "paid": "[Udemy – REST APIs](https://www.udemy.com/course/api-with-postman-for-absolute-beginners/)"
        },
        "json": {
            "free": "[W3Schools – JSON](https://www.w3schools.com/js/js_json_intro.asp)",
            "paid": "[LinkedIn – Learning JSON](https://www.linkedin.com/learning/json-essential-training)"
        },
        "node.js": {
            "free": "[Node.js Docs](https://nodejs.org/en/docs)",
            "paid": "[Udemy – Node.js Bootcamp](https://www.udemy.com/course/the-complete-nodejs-developer-course-2/)"
        },
        "express": {
            "free": "[MDN – Express Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs)",
            "paid": "[Udemy – Express Course](https://www.udemy.com/course/nodejs-express-mongodb-bootcamp/)"
        },
        "postman": {
            "free": "[Postman Learning Center](https://learning.postman.com/)",
            "paid": "[Udemy – Postman Guide](https://www.udemy.com/course/postman-the-complete-guide/)"
        }
    })
})

#Role 25: Machine learning engineer
dataset.append({
    "job_role": "machine learning engineer",
    "core_skills": "python, machine learning, scikit-learn, pandas, model deployment",
    "optional_skills": "tensorflow, keras, flask, docker, statistics",
    "skill_resources": json.dumps({
        "python": {
            "free": "[freeCodeCamp – Python](https://www.freecodecamp.org/learn/)",
            "paid": "[Udemy – Python Mega Course](https://www.udemy.com/course/the-python-mega-course/)"
        },
        "machine learning": {
            "free": "[Google ML Crash Course](https://developers.google.com/machine-learning/crash-course)",
            "paid": "[Coursera – Machine Learning (Andrew Ng)](https://www.coursera.org/learn/machine-learning)"
        },
        "scikit-learn": {
            "free": "[Scikit-learn Docs](https://scikit-learn.org/stable/user_guide.html)",
            "paid": "[Udemy – Sklearn Hands-On](https://www.udemy.com/course/feature-selection-for-machine-learning/)"
        },
        "pandas": {
            "free": "[Pandas Documentation](https://pandas.pydata.org/docs/)",
            "paid": "[DataCamp – Pandas Foundations](https://www.datacamp.com/courses/pandas-foundations)"
        },
        "model deployment": {
            "free": "[MLflow Guide](https://mlflow.org/docs/latest/index.html)",
            "paid": "[Coursera – Model Deployment](https://www.coursera.org/learn/deploying-machine-learning-models)"
        }
    })
})


#converting into csv
for row in dataset:
    row['skill_resources'] = json.dumps(row['skill_resources'])

df = pd.DataFrame(dataset)
df.to_csv("skillspread_dataset.csv", index=False)
df.to_excel("skillspread_dataset.xlsx", index=False)