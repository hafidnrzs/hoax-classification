import streamlit as st
from time import sleep

# Simulasi fungsi klasifikasi hoax
def classify_text(text):
    """
    Fungsi ini akan mensimulasikan klasifikasi teks menjadi 'Hoax' atau 'Not Hoax'.
    Dalam implementasi nyata, fungsi ini dapat memanggil model machine learning.
    """
    if len(text.strip()) == 0:
        return "Masukkan teks terlebih dahulu."
    elif "hoax" in text.lower():
        return "Hoax"
    else:
        return "Not Hoax"

# Pengaturan halaman
st.set_page_config(
    page_title="Hoax Classification",
    layout="centered",
    page_icon=":red_car:"
)


st.title("Hoax Classification")
st.write("Aplikasi ini membantu mengklasifikasikan apakah suatu teks mengandung hoax atau tidak.")


input_text = st.text_area("Masukkan teks untuk klasifikasi:", height=100)


if st.button("Klasifikasikan"):
    if input_text:
        # Menampilkan progress bar
        progress_bar = st.progress(0) 
        status_text = st.empty()  
        status_text.text("Sedang memproses...")

        for percent in range(101): 
            sleep(0.03)  
            progress_bar.progress(percent)

        
        status_text.text("Proses selesai!")

        
        result = classify_text(input_text)

        
        st.subheader("Hasil Klasifikasi:")
        if result == "Hoax":
            st.markdown(
                f"""
                <div style="color: white; background-color: red; font-size: 20px; border-radius: 12px; padding: 10px; text-align: center; width: fit-content;">
                    <b>{result}</b>
                </div>
                """, 
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div style="color: white; background-color: green; font-size: 20px; border-radius: 12px; padding: 10px; text-align: center; width: fit-content;">
                    <b>{result}</b>
                </div>
                """, 
                unsafe_allow_html=True
            )

        
        sleep(1)
        progress_bar.empty()
        status_text.empty()
    else:
        st.error("Harap masukkan teks sebelum melakukan klasifikasi.")


