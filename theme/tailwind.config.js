/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./templates/**/*.{html,js}"],
    theme: {
        fontFamily: {
            'sans': ['Poppins', 'sans-serif'],
            'serif': ['Playfair Display', 'serif'],
        },
        listStyleType: {
            none: 'none',
            disc: 'disc',
            square: 'square',
        },
        extend: {
            content: {
                'searchIcon': 'url("images/search.svg")',
                'searchBlackIcon': 'url("images/search-black.svg")',
                'coursesIcon': 'url("images/courses.svg")',
                'coursesWhiteIcon': 'url("images/courses-white.svg")',
                'forumIcon': 'url("images/forum.svg")',
                'forumWhiteIcon': 'url("images/forum-white.svg")',
                'hireIcon': 'url("images/hire-me.svg")',
                'hireWhiteIcon': 'url("images/hire-me-white.svg")',
                'aboutIcon': 'url("images/about.svg")',
                'aboutWhiteIcon': 'url("images/aboutWhite.svg")',
                'blogIcon': 'url("images/blog.svg")',
                'blogWhiteIcon': 'url("images/blog-white.svg")',
                'booksIcon': 'url("images/books.svg")',
                'booksWhiteIcon': 'url("images/books-white.svg")',
                'arrowBlue': 'url("images/arrow-blue.svg")',
                'profile': 'url("images/profile.svg")',
                'calendar': 'url("images/calendar.svg")',
                'tag': 'url("images/tag.svg")',
                'article': 'url("images/article.svg")',
            },
            backgroundImage: {
                'arrow': 'url("images/arrow-blue.svg")',
            },
        },
    },
    plugins: [],
}

