var language = {
    ar: {

        home: "الصفحة الرئيسية",
        btnlanguage: "English",
        about: "من نحن",
        rules: "الشروط و الاحكام",
        account: "حسابي",
        goals: "ألاهداف",
        goal: `المملكه العربيه السعوديه ثرية بالمناطق و الحضارات و الاثار التاريخية و المعالم السياحية و نحن هنا في هذا الموقع نهدف الى اظهار وطننا الحبيب بصورة حسنة و ابراز هويتنا و ثقافتنا و معالما الحضارية من خلاله و تسليط الضوء على مناطق رائعة غير معروفة او لم تكتشف بعد و التشجيع على السياحة الداخلية.`,
        seemore: "شاهد أيضا",
        aboutLand: "عن المعلم",
        aboutC: `
        نحن مجموعة من المطورين و المصممين أسسنا هذا الموقع بتاريخ 2021/10
        للتواصل معنا يرجى التواصل عبر الأيميل التالي : m3alem.ksa@gmail.com`,
        rule: [ 
            "يمنع تنزيل محتوى فيه اساءة للوطن",
            "الالتزام بالاداب و الذوق العام و عدم تنزيل محتوى به لبس خادش للحياء",
            "يمنع نشر محتوى غير قانوني يستهدف الترويج لممارسات غير شرعية ينطوي عليها مسؤولية مدنية",
            "يمنع انتحال المستخدم لهوية أحد الأفراد",
            "يمنع استخدام الموقع في نشر محتوى لا علافة له بالخدمة المقدمة",
            "يمنع تمثيل أحد المؤسسات أو الهيئات بدون أن يكون المستخدم مخولا بادعاء هذا التمثيل",
            "يمنع نشر مواد تضر بالملكية الفكرية لأصحابها و تدخل في اطار سرقتها",
            "صاحب الموقع له الحق في حذف محتواك أو حسابك الشخصي في حال الاخلال بأي من الشروط و الأحكام أعلاه",
            "The owner of the site has the right to delete your content or personal account when breaching any of the above terms and conditions",
        ],
        placeName: "المكان",
        landmarkName: "المعلم",
        cityName: "المدينة",
        login: "تسجيل الدخول",
        logout: "تسجيل الخروج",

    },
    en: {
    
        btnlanguage: "عربي",
        home: "Home",
        about: "About",
        rules: "Rules",
        account: "Account",
        goals: "Goals",
        goal: `The Kingdom of Saudi Arabia is rich in regions, civilizations, historical monuments and tourist attractions. Our goal on this site is to show our beloved country in a good way, highlight our identity, culture and cultural landmarks through it, and shed the light on some wonderful areas unknown or isn't discovered yet, and to encourage people on domestic tourism.`,
        seemore: "See more",
        aboutLand: "About land mark",
        aboutC: `We are a group of developers and designers who established this website at 10/2021
        To contact us, please reach us via the following email:
       m3alem.ksa@gmail.com`,
       rule: [ 
        "It is forbidden to upload any content that offends the country",
        "Commitment to etiquettes and public taste, and not to upload content while wearing non modesty clothing",
        "It is forbidden to upload illegal content aimed at promoting illegal practices that involve civil liability",
        "It is forbidden to distort the public image of a person",
        "It is forbidden to impersonation of another person's identity",
        "It is prohibited to use the site to upload unrelated content to the service provided",
        "It is prohibited to represent an institution or organization without the user being authorized to such representation",
        "It is prohibited to upload content that harm the intellectual property of their owners and falls within the theft",
        "The owner of the site has the right to delete your content or personal account when breaching any of the above terms and conditions",
        ],
        placeName: "Place",
        cityName: "City",
        landmarkName: "Landmark",
        login: "Login",
        logout: "Logout"


    }
}



var btnlanguage = document.getElementById("btnlanguage");
function lang(l)
{
    switch (l)
    {      
        case "en": 
            localStorage.setItem("language", "en");
            btnlanguage.onclick = function () { lang("ar"); };
        break;	
        default:
            if (!document.getElementById("rtl")) 
            {
                let rtl = document.createElement("link");
                rtl.id = "rtl";
                rtl.href = "/static/css/style-rtl.css";
                rtl.rel = "stylesheet";
                document.getElementsByTagName("head")[0].appendChild(rtl);
            }
            localStorage.setItem("language", "ar");
            btnlanguage.onclick = function () { lang("en"); }
    }
    changeLanguage(getLanguage());
}



function getLanguage()
{
    var languageWeb = language.ar;
    switch (localStorage.getItem("language"))
    {   
        case "en":
            languageWeb = language.en;
            btnlanguage.onclick = function () { lang("ar"); };
            if (document.getElementById("rtl")) document.getElementById("rtl").remove();
        break;

        default:
            languageWeb = language.ar;
            btnlanguage.onclick = function () { lang("en"); };
    }
    return languageWeb
}

function changeLanguage(language=language.ar)
{
    for (let [key, value] of Object.entries(language))
    {
        if (!document.getElementById(key)) continue

        let element = document.getElementById(key);
        
        if (element.id == "rule")
        {
            let index = 0;
            value.forEach(rulex => {
                element.children[index++].textContent = rulex;
            });
        }
            
        else
            element.textContent = value;
    }
}

changeLanguage(getLanguage());
