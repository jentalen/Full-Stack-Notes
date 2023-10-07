# 10/06/23 Notes
# I watched the following YouTube video
codedamn_url = "https://www.youtube.com/watch?v=SgVXmtMUjbI&t=191s"
programming_guru_url = "https://www.youtube.com/watch?v=NHNm7VzYvuY"
tech_projects_url = "https://www.youtube.com/watch?v=vRxfnHtCxEo"

def oct0623_comments():
    comments = f'''
    Front End 
    Profiling (performance) how to speed up the build
    WASM
    Typescript
    Tailwind
    React
    Devtools
    HTML
    CSS
    Javascript ES6+
    He stated to now use Var, Callbacks. Instead, use sync await, Modern Javascript syntax and declarative methods

    I watched the following YouTube video for a list of front end and back end things to know: {codedamn_url}
    I watched the following YouTube video to learn how to install node.js into vs code: {programming_guru_url}
    I watched the following YouTube video to learn push my vs code projects to github: {tech_projects_url}

    Backend
    Linux (Bash)
    Networking
    Caching (Redis)
    Web security
    Node.js or rust or python
    api - make note to deep dive into the information
    REST clients rest API Rest server REST request REST response
    cloud provider AWS digital ocean
    Typescript backend too, wonder why
    HTTP

    MISC
    CI/CD github
    cypress.io
    NPM and Yarn
    linters, webpack
    mongoDB atlas NoSQL
    PlanetScale SQL
    Vercel

    I am going to include GitHub and GIT as well.
    '''

    print(comments)

# Call the function to print the comments
oct0623_comments()



name = "Alice"

# Define a function
def greet(person_name):
    print("Hello, " + person_name + "!")

# Call the function
greet(name)  # This will print "Hello, Alice!"