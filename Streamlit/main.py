import pickle
import streamlit as st

# loading the trained model
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

page_bg_img = '''
<style>
body {
background-image: url("https://www.pixelstalk.net/wp-content/uploads/2016/10/Download-Free-Aesthetic-HD-Images.jpg");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

@st.cache()
# defining the function which will make the prediction using the data which the user inputs
def prediction(KlasifikasiId, TajukLatihanId, TempatLatihanId, JabatanId, JumlahJam):
    # Pre-processing user input
    if KlasifikasiId == "PBP":
        KlasifikasiId = 0
    elif KlasifikasiId == "CPD":
        KlasifikasiId = 1
    elif KlasifikasiId == "KAP":
        KlasifikasiId = 2

    if TajukLatihanId == "FORUM BULAN PENDIDIK I - UNIVERSITY FOR SOCIETY":
        TajukLatihanId = 0
    elif TajukLatihanId == "FORUM BULAN PENDIDIK II - KECEMERLANGAN PERTANIAN MELAHIRKAN USAHAWAN":
        TajukLatihanId = 1
    elif TajukLatihanId == "KURSUS ASAS PENGAJARAN (KAP) SIRI 1/2020":
        TajukLatihanId = 2
    elif TajukLatihanId == "KURSUS ASAS PENGAJARAN (KAP) SIRI 2/2020":
        TajukLatihanId = 3
    elif TajukLatihanId == "KURSUS CREATING INTERACTIVE CONTENT WITH H5P":
        TajukLatihanId = 4
    elif TajukLatihanId == "KURSUS DEVELOPING WINNING TEACHING E-PORTFOLIO FOR ACADEMICS":
        TajukLatihanId = 5
    elif TajukLatihanId == "KURSUS EDUCATIONAL RESEARCH DESIGN":
        TajukLatihanId = 6
    elif TajukLatihanId == "KURSUS PUTRABLAST V3.8 (SIRI 1 - FK & FRSB)":
        TajukLatihanId = 7
    elif TajukLatihanId == "KURSUS PUTRABLAST V3.8 (SIRI 2 - FBMK & FSKTM)":
        TajukLatihanId = 8
    elif TajukLatihanId == "KURSUS PUTRABLAST V3.8 (SIRI 3 - FEP & FPP)":
        TajukLatihanId = 9
    elif TajukLatihanId == "KURSUS PUTRABLAST V3.8 (SIRI 4 - FEM & FS)":
        TajukLatihanId = 10
    elif TajukLatihanId == "KURSUS PUTRABLAST V3.8 (SIRI 5 - FBSB & FSTM)":
        TajukLatihanId = 11
    elif TajukLatihanId == "KURSUS PUTRABLAST V3.8 (SIRI 6 - FH & FPAS)":
        TajukLatihanId = 12
    elif TajukLatihanId == "KURSUS PUTRABLAST V3.8 (SIRI 7 - FP & FBMK)":
        TajukLatihanId = 13
    elif TajukLatihanId == "KURSUS SISTEM PUTRABLAST V3.8 (SIRI 8 - FPSK & FPV)":
        TajukLatihanId = 14
    elif TajukLatihanId == "KURSUS SISTEM PUTRABLAST V3.8 (SIRI 9 - FSPM, UPMKB)":
        TajukLatihanId = 15
    elif TajukLatihanId == "KURSUS VISUAL MESSAGE DESIGN: CRAFTING INFOGRAPHICS FOR PRESENTATIONS":
        TajukLatihanId = 16
    elif TajukLatihanId == "MAJLIS PERASMIAN & ASPIRASI NC SEMPENA BULAN PENDIDIK UPM 2020":
        TajukLatihanId = 17
    elif TajukLatihanId == "PERTANDINGAN AMALAN TERBAIK INOVASI P&P ANTARA FAKULTI/ PUSAT PENGAJIAN UPM 2020":
        TajukLatihanId = 18
    elif TajukLatihanId == "PUTRAFLEX: KURIKULUM FLEKSIBEL UPM":
        TajukLatihanId = 19
    elif TajukLatihanId == "SESI PERKONGSIAN AMALAN TERBAIK PELAKSANAAN PUTRAMOOC":
        TajukLatihanId = 20
    elif TajukLatihanId == "SESI PERKONGSIAN AMALAN TERBAIK SULAM@UPM":
        TajukLatihanId = 21
    elif TajukLatihanId == "SESI PERKONGSIAN INOVASI P&P DARIPADA PENYELIDIKAN GIPP":
        TajukLatihanId = 22
    elif TajukLatihanId == "WACANA - INSTRUCTIONAL LEADERSHIP OF HIGHER EDUCATION TEACHING AND LEARNING & MAJLIS PENUTUPAN BULAN PENDIDIK UPM 2020":
        TajukLatihanId = 23
    elif TajukLatihanId == "WEBINAR - REIMAGINE AND REDESIGN ONLINE LEARNING EXPERIENCE":
        TajukLatihanId = 24


    if TempatLatihanId == "PLATFORM DALAM TALIAN: ZOOM & YOUTUBE":
        TempatLatihanId = 0
    elif TempatLatihanId == "BILIK LATIHAN EXA, IDEC ALPHA, PUTRA INFOPORT, UPM":
        TempatLatihanId = 1
    elif TempatLatihanId == "DEWAN SEMINAR AL-FARABI, FEM, UPM":
        TempatLatihanId = 2
    elif TempatLatihanId == "MAKMAL D ICT, UPMKB":
        TempatLatihanId = 3
    elif TempatLatihanId == "PLATFORM DALAM TALIAN: ZOOM MEETING":
        TempatLatihanId = 4
    elif TempatLatihanId == "PUTRA LEARNING SPACE (PLS), CADE, UPM":
        TempatLatihanId = 5


    if JabatanId == "BAHAGIAN HAL EHWAL PELAJAR":
        JabatanId = 0
    elif JabatanId == "FAKULTI BAHASA MODEN DAN KOMUNIKASI":
        JabatanId = 1
    elif JabatanId == "FAKULTI BIOTEKNOLOGI DAN SAINS BIOMOLEKUL":
        JabatanId = 2
    elif JabatanId == "FAKULTI EKOLOGI MANUSIA":
        JabatanId = 3
    elif JabatanId == "FAKULTI KEJURUTERAAN":
        JabatanId = 4
    elif JabatanId == "FAKULTI PENGAJIAN ALAM SEKITAR":
        JabatanId = 5
    elif JabatanId == "FAKULTI PENGAJIAN PENDIDIKAN":
        JabatanId = 6
    elif JabatanId == "FAKULTI PERHUTANAN DAN ALAM SEKITAR":
        JabatanId = 7
    elif JabatanId == "FAKULTI PERTANIAN":
        JabatanId = 8
    elif JabatanId == "FAKULTI PERUBATAN DAN SAINS KESIHATAN":
        JabatanId = 9
    elif JabatanId == "FAKULTI PERUBATAN VETERINAR":
        JabatanId = 10
    elif JabatanId == "FAKULTI REKABENTUK DAN SENIBINA":
        JabatanId = 11
    elif JabatanId == "FAKULTI SAINS":
        JabatanId = 12
    elif JabatanId == "FAKULTI SAINS DAN TEKNOLOGI MAKANAN":
        JabatanId = 13
    elif JabatanId == "FAKULTI SAINS KOMPUTER DAN TEKNOLOGI MAKLUMAT":
        JabatanId = 14
    elif JabatanId == "INSTITUT KAJIAN PERLADANGAN":
        JabatanId = 15
    elif JabatanId == "JABATAN CANSELERI":
        JabatanId = 16
    elif JabatanId == "JABATAN SAINS DAN TEKNOLOGI":
        JabatanId = 17
    elif JabatanId == "JABATAN SAINS HAIWAN DAN PERIKANAN":
        JabatanId = 18
    elif JabatanId == "JABATAN SAINS PERHUTANAN":
        JabatanId = 19
    elif JabatanId == "JABATAN SAINS SOSIAL DAN PENGURUSAN":
        JabatanId = 20
    elif JabatanId == "JABATAN SAINS TANAMAN":
        JabatanId = 21
    elif JabatanId == "PUSAT ASASI SAINS PERTANIAN":
        JabatanId = 22
    elif JabatanId == "PUSAT ISLAM":
        JabatanId = 23
    elif JabatanId == "PUSAT PEMAJUAN KOMPETENSI BAHASA":
        JabatanId = 24
    elif JabatanId == "PUSAT PEMBANGUNAN AKADEMIK":
        JabatanId = 25
    elif JabatanId == "PUSAT PEMBANGUNAN MAKLUMAT DAN KOMUNIKASI":
        JabatanId = 26
    elif JabatanId == "PUSAT TRANSFORMASI KOMUNITI UNIVERSITI":
        JabatanId = 27
    elif JabatanId == "SEKOLAH PERNIAGAAN DAN EKONOMI":
        JabatanId = 28


    # Making predictions
    prediction = classifier.predict([[KlasifikasiId, TajukLatihanId, TempatLatihanId, JabatanId, JumlahJam]])

    if prediction == 0:
        pred = 'Low'
    elif prediction == 1:
        pred = 'Middle'
    else:
        pred = 'High'

    return pred

# this is the main function in which we define our webpage
def main():
    # front end elements of the web page
    html_temp = """ 
    <div style ="background-color:pink;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Score Prediction App</h1> 
    </div> 
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)

    KlasifikasiId = st.selectbox("Klasifikasi", ["PBP", "KAP", "CPD"])

    TajukLatihanId = st.selectbox("Tajuk Latihan", ["FORUM BULAN PENDIDIK I - UNIVERSITY FOR SOCIETY",
                                                           "FORUM BULAN PENDIDIK II - KECEMERLANGAN PERTANIAN MELAHIRKAN USAHAWAN",
                                                           "MAJLIS PERASMIAN & ASPIRASI NC SEMPENA BULAN PENDIDIK UPM 2020",
                                                           "PERTANDINGAN AMALAN TERBAIK INOVASI P&P ANTARA FAKULTI/ PUSAT PENGAJIAN UPM 2020",
                                                           "PUTRAFLEX: KURIKULUM FLEKSIBEL UPM",
                                                           "SESI PERKONGSIAN AMALAN TERBAIK PELAKSANAAN PUTRAMOOC",
                                                           "SESI PERKONGSIAN AMALAN TERBAIK SULAM@UPM",
                                                           "SESI PERKONGSIAN INOVASI P&P DARIPADA PENYELIDIKAN GIPP",
                                                           "WACANA - INSTRUCTIONAL LEADERSHIP OF HIGHER EDUCATION TEACHING AND LEARNING & MAJLIS PENUTUPAN BULAN PENDIDIK UPM 2020"
                                                        , "WEBINAR - REIMAGINE AND REDESIGN ONLINE LEARNING EXPERIENCE", "KURSUS ASAS PENGAJARAN (KAP) SIRI 1/2020"
                                                        , "KURSUS ASAS PENGAJARAN (KAP) SIRI 2/2020", "KURSUS CREATING INTERACTIVE CONTENT WITH H5P",
                                                           "KURSUS DEVELOPING WINNING TEACHING E-PORTFOLIO FOR ACADEMICS",
                                                           "KURSUS EDUCATIONAL RESEARCH DESIGN"
                                                        ,  "KURSUS PUTRABLAST V3.8 (SIRI 1 - FK & FRSB)", "KURSUS PUTRABLAST V3.8 (SIRI 2 - FBMK & FSKTM)",
                                                           "KURSUS PUTRABLAST V3.8 (SIRI 3 - FEP & FPP)",
                                                           "KURSUS PUTRABLAST V3.8 (SIRI 4 - FEM & FS)",
                                                           "KURSUS PUTRABLAST V3.8 (SIRI 5 - FBSB & FSTM)",
                                                           "KURSUS PUTRABLAST V3.8 (SIRI 6 - FH & FPAS)",
                                                           "KURSUS PUTRABLAST V3.8 (SIRI 7 - FP & FBMK)",
                                                           "KURSUS SISTEM PUTRABLAST V3.8 (SIRI 8 - FPSK & FPV)",
                                                           "KURSUS SISTEM PUTRABLAST V3.8 (SIRI 9 - FSPM, UPMKB)",
                                                           "KURSUS VISUAL MESSAGE DESIGN: CRAFTING INFOGRAPHICS FOR PRESENTATIONS"])


    TempatLatihanId = st.selectbox('Tempat Latihan',("PLATFORM DALAM TALIAN: ZOOM & YOUTUBE","BILIK LATIHAN EXA, IDEC ALPHA, PUTRA INFOPORT, UPM",
                                                   "DEWAN SEMINAR AL-FARABI, FEM, UPM", "MAKMAL D ICT, UPMKB", "PLATFORM DALAM TALIAN: ZOOM MEETING",
                                                    "PUTRA LEARNING SPACE (PLS), CADE, UPM", ))
    JabatanId = st.selectbox('Jabatan',("FAKULTI BAHASA MODEN DAN KOMUNIKASI","BAHAGIAN HAL EHWAL PELAJAR",
                                        "FAKULTI BIOTEKNOLOGI DAN SAINS BIOMOLEKUL", "FAKULTI EKOLOGI MANUSIA",
                                        "FAKULTI KEJURUTERAAN", "FAKULTI PENGAJIAN PENDIDIKAN", "FAKULTI PERHUTANAN DAN ALAM SEKITAR",
                                        "FAKULTI PERTANIAN", "FAKULTI PERUBATAN DAN SAINS KESIHATAN" , "FAKULTI PERUBATAN VETERINAR",
                                        "FAKULTI REKABENTUK DAN SENIBINA", "FAKULTI SAINS", "FAKULTI SAINS DAN TEKNOLOGI MAKANAN",
                                        "FAKULTI SAINS KOMPUTER DAN TEKNOLOGI MAKLUMAT", "INSTITUT KAJIAN PERLADANGAN",
                                        "JABATAN CANSELERI", "JABATAN SAINS DAN TEKNOLOGI", "JABATAN SAINS HAIWAN DAN PERIKANAN", "JABATAN SAINS PERHUTANAN",
                                        "JABATAN SAINS SOSIAL DAN PENGURUSAN", "JABATAN SAINS TANAMAN", "PUSAT ASASI SAINS PERTANIAN",
                                        "PUSAT ISLAM", "PUSAT PEMAJUAN KOMPETENSI BAHASA", "PUSAT PEMBANGUNAN AKADEMIK",
                                        "PUSAT PEMBANGUNAN MAKLUMAT DAN KOMUNIKASI", "PUSAT TRANSFORMASI KOMUNITI UNIVERSITI",
                                        "SEKOLAH PERNIAGAAN DAN EKONOMI"))


    JumlahJam = st.selectbox('Jumlah Jam', (2, 3, 4, 6, 7, 17, 25, 28, 28, 29,32,34,35,36,42))

    result = ""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        result = prediction(KlasifikasiId, TajukLatihanId, TempatLatihanId, JabatanId, JumlahJam)
        st.success('Your Score is {}'.format(result))


if __name__ == '__main__':
    main()
