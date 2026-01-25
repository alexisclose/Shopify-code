
      document.addEventListener('DOMContentLoaded', function () {
        window.addEventListener('scroll', function () {
          const scrollTop = window.scrollY;
          const docHeight = document.documentElement.scrollHeight - window.innerHeight;
          const scrollPercent = (scrollTop / docHeight) * 100;

          if (scrollPercent >= 5) {
            document.body.classList.add('scroll-cls');
          } else {
            document.body.classList.remove('scroll-cls');
          }
        });
      });
    