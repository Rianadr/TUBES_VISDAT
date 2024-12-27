import streamlit as st
import pandas as pd
import plotly.express as px

# Function to load data
def load_data():
    try:
        data = pd.read_csv("THE World University Rankings 2016-2025.csv")
        return data
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

# Title of the application
st.title("World University Rankings Explorer (2016-2025)")

# Load data
data = load_data()

if data is not None:
    # Check if required columns are present in the dataset
    required_columns = ["Name", "Year", "Rank", "Country", "Teaching", "Research Environment", "Student Population"]
    missing_columns = [col for col in required_columns if col not in data.columns]

    if missing_columns:
        st.error(f"The following required columns are missing from the dataset: {missing_columns}")
    else:
        # Sidebar navigation menu
        st.sidebar.title("Menu")
        menu = ["Dataset Preview", "Top 10 Universities", "University Performance", 
                "Distribution of Universities by Country", "Student Population Growth", "Comparison Between University"]
        choice = st.sidebar.radio("Navigate to:", menu)

        # Page 1: Dataset Preview
        if choice == "Dataset Preview":
            st.subheader("📊 Dataset Preview")
            st.markdown("""
                Selamat datang di **Dataset Preview**! 🌟
                Di sini, Anda dapat menjelajahi beberapa baris pertama dari dataset **THE World University Rankings (2016-2025)**. 
                Ini adalah kesempatan Anda untuk memeriksa apakah semua data telah dimuat dengan benar dan mendapatkan gambaran awal tentang universitas yang termasuk! 👩‍🎓👨‍🎓

                **Apa yang ada dalam Dataset?** 📚
                - **Rank**: Peringkat global universitas.
                - **Name**: Nama universitas.
                - **Country**: Negara tempat universitas berada.
                - **Student Population**: Total jumlah mahasiswa di universitas.
                - **Students to Staff Ratio**: Jumlah mahasiswa per staf.
                - **International Students**: Persentase mahasiswa internasional.
                - **Female to Male Ratio**: Rasio perempuan terhadap laki-laki.
                - **Overall Score**: Skor dari 100 berdasarkan pengajaran, lingkungan penelitian, kualitas penelitian, dampak industri, dan pandangan internasional.
                - **Teaching**: Skor dari 100 yang mengukur kualitas pengajaran universitas.
                - **Research Environment**: Skor dari 100 yang mengukur kemampuan universitas untuk menyediakan lingkungan yang kondusif untuk penelitian.
                - **Research Quality**: Skor dari 100 yang mengukur kualitas penelitian yang dihasilkan oleh universitas, termasuk publikasi, sitasi, dan dampak penelitian.
                - **Industry Impact**: Skor dari 100 yang mencerminkan seberapa baik universitas berkontribusi terhadap industri, termasuk kolaborasi dengan perusahaan dan dampak penelitian terhadap praktik industri.
                - **International Outlook**: Skor dari 100 yang mengukur seberapa internasional universitas, termasuk proporsi mahasiswa internasional dan kolaborasi penelitian internasional.
                - **Year**: Tahun di mana data peringkat universitas tersebut diambil, mencakup periode dari 2016 hingga 2025.

                **Mengapa ini penting?** 🤔
                Memahami dataset membantu Anda memahami lanskap pendidikan tinggi global dan faktor-faktor yang berkontribusi pada peringkat universitas. 
                Apakah Anda seorang mahasiswa, pendidik, atau peneliti, informasi ini sangat penting untuk membuat keputusan yang tepat! 🌍

                Mari kita selami dan lihat apa yang ditawarkan data ini! 🔍
            """)

            # Display the dataset preview
            st.dataframe(data.head())


        # Page 2: Top 10 Universities
        elif choice == "Top 10 Universities":
            st.subheader("🏆 Top 10 Universities by Year")
            st.markdown("""
                Selamat datang di **Top 10 Universities by Year**! 🎓✨
                Di sini, Anda dapat menemukan institusi elit yang memimpin dalam pendidikan tinggi untuk tahun tertentu. 
                Pilih tahun dari menu dropdown di bawah untuk mengungkap universitas-universitas yang berhasil masuk ke peringkat teratas! 🌍📈

                **Mengapa Menjelajahi 10 Teratas?** 🤔
                - **Pendidikan Berkualitas**: Universitas-universitas ini diakui karena pengajaran dan penelitian yang luar biasa.
                - **Dampak Global**: Mereka memainkan peran penting dalam membentuk masa depan pendidikan dan inovasi di seluruh dunia.
                - **Peluang Karir**: Lulusan dari universitas yang teratas dapat membuka pintu untuk berbagai jalur karir dan peluang jaringan. 🚀

                **Cara Menggunakan Fitur Ini**: 
                1. Pilih tahun dari menu dropdown.
                2. Amati peringkat dan lihat universitas mana yang berada di garis depan keunggulan akademis.
                3. Klik pada batang di grafik untuk mempelajari lebih lanjut tentang masing-masing universitas! 🔍

                Mari kita selami peringkat dan lihat siapa yang berhasil masuk tahun ini! 🥇
            """)

            selected_year = st.selectbox("Select a Year:", options=sorted(data["Year"].unique()))
            top_10_data = data[data["Year"] == selected_year].nsmallest(10, "Rank")

            if not top_10_data.empty:
                # Sort the data by Rank for better visualization
                top_10_data = top_10_data.sort_values(by="Rank")

                # Create a horizontal bar chart
                fig = px.bar(
                    top_10_data,
                    x="Rank",
                    y="Name",
                    title=f"Top 10 Universities in {selected_year}",
                    labels={"Name": "University", "Rank": "Rank"},
                    text="Rank",
                    orientation="h",  # Horizontal bar chart
                    color="Rank",  # Color by rank for better visual distinction
                    color_continuous_scale=px.colors.sequential.Viridis  # Use a sequential color scale
                )
                
                # Reverse the order of the y-axis to show the best rank at the top
                fig.update_yaxes(autorange="reversed")

                fig.update_traces(texttemplate='%{text}', textposition='outside')  # Show rank outside the bars
                fig.update_layout(xaxis=dict(title='Rank (1 is best)', autorange='reversed'))  # Clear x-axis title
                st.plotly_chart(fig)
            else:
                st.warning(f"No data available for the year {selected_year}.")




        # Page 3: University Performance
        elif choice == "University Performance":
            st.subheader("📈 University Performance Over Time")
            st.markdown("""
                Penasaran bagaimana universitas favorit Anda telah berprestasi selama bertahun-tahun? 📅🔍
                Visualisasi ini melacak tren peringkat universitas tertentu dari 2016 hingga 2025. 
                Pilih universitas dari menu dropdown di bawah untuk melihat apakah mereka telah mencapai puncak baru atau menghadapi tantangan di sepanjang jalan! 🚀📉
                
                **Mengapa Ini Penting?** 🤔
                Memahami kinerja universitas dari waktu ke waktu dapat memberikan wawasan tentang pertumbuhan, reputasi, dan kualitas pendidikan yang ditawarkannya. 
                Apakah Anda seorang calon mahasiswa, alumni, atau hanya seorang penggemar pendidikan, informasi ini sangat berharga! 🎓✨
            """)

            university = st.selectbox("Select a University:", options=data["Name"].unique())
            uni_data = data[data["Name"] == university]

            if not uni_data.empty:
                fig = px.line(
                    uni_data,
                    x="Year",
                    y="Rank",
                    title=f"📊 Ranking Trend of {university} Over Time",
                    labels={"Rank": "Rank", "Year": "Year"},
                    markers=True
                )
                fig.update_yaxes(autorange="reversed")  # Best rank (1) at the top
                st.plotly_chart(fig)

                st.markdown(f"""
                **Insight Utama untuk {university}:** 🔑
                - **Peringkat Terbaik yang Dicapai:** {uni_data['Rank'].min()} di {uni_data.loc[uni_data['Rank'].idxmin(), 'Year']}
                - **Peringkat Saat Ini:** {uni_data['Rank'].iloc[-1]} di {uni_data['Year'].iloc[-1]}
                - **Tren Keseluruhan:** {'📉 Menurun' if uni_data['Rank'].iloc[-1] > uni_data['Rank'].iloc[0] else '📈 Meningkat'}
                
                Tren ini dapat membantu Anda memahami lintasan universitas dan kedudukannya dalam lanskap pendidikan global. 🌍
            """)
            else:
                st.warning("No data available for the selected university.")


        # Page 4: Distribution of Universities by Country
        elif choice == "Distribution of Universities by Country":
            st.subheader("🌍 Distribution of Universities by Country")
            st.markdown("""
                Visualisasi ini menunjukkan jumlah universitas dari setiap negara yang masuk dalam peringkat dunia 
                selama periode 2016-2025. Anda dapat melihat bagaimana distribusi universitas berubah dari tahun ke tahun. 📈✨

                **Mengapa Ini Penting?** 🤔
                - **Pendidikan Global**: Memahami distribusi universitas membantu kita melihat kekuatan pendidikan di berbagai negara.
                - **Tren Pendidikan**: Analisis ini dapat mengungkap tren dalam pendidikan tinggi, seperti pertumbuhan universitas baru atau penurunan di negara tertentu.
                - **Perencanaan Kebijakan**: Data ini dapat membantu pembuat kebijakan dalam merumuskan strategi untuk meningkatkan pendidikan tinggi. 🏫

                **Cara Menggunakan Visualisasi Ini**: 
                1. Amati peta untuk melihat jumlah universitas di setiap negara.
                2. Gunakan animasi untuk melihat perubahan dari tahun ke tahun.
                3. Pertimbangkan bagaimana faktor-faktor seperti ekonomi dan kebijakan pendidikan dapat mempengaruhi jumlah universitas. 🔍
            """)

            # Menghitung jumlah universitas per negara
            count_data = data.groupby(["Year", "Country"]).size().reset_index(name="Count")

            # Visualisasi peta menggunakan choropleth
            fig = px.choropleth(
                count_data,
                locations="Country",  # Kolom negara
                locationmode="country names",  # Menggunakan nama negara
                color="Count",  # Data yang akan divisualisasikan
                animation_frame="Year",  # Animasi berdasarkan tahun
                title="📊 Jumlah Universitas per Negara dari Tahun ke Tahun",
                labels={"Count": "Jumlah Universitas", "Country": "Negara"},
                color_continuous_scale=px.colors.sequential.Plasma,
                projection="natural earth"  # Menggunakan proyeksi peta yang lebih menarik
            )

            # Menambahkan anotasi untuk meningkatkan pemahaman
            fig.update_layout(
                title_x=0,  # Align title to the left
                title_xanchor='left',  # Anchor the title to the left
                title_font=dict(size=24),  # Increase title font size
                geo=dict(
                    showcoastlines=True,
                    coastlinecolor="Black",
                    showland=True,
                    landcolor="lightgray",
                    subunitcolor="Black",
                    countrycolor="Black"
                ),
                margin=dict(l=0, r=0, t=40, b=0)  # Adjust margins
            )

            # Menampilkan grafik
            st.plotly_chart(fig)

            # Key insights section
            st.markdown("""
                **Insight Utama**: 🔑
                - Negara dengan jumlah universitas terbanyak menunjukkan komitmen terhadap pendidikan tinggi.
                - Perubahan jumlah universitas dari tahun ke tahun dapat mencerminkan kebijakan pendidikan dan investasi dalam sektor pendidikan.
                - Amati negara-negara yang mengalami pertumbuhan pesat dan yang mungkin mengalami penurunan. 📉
            """)

        # Page 5: Student Population Growth
        elif choice == "Student Population Growth":
            st.subheader("👩‍🎓📈 Student Population Growth Over Time")
            st.markdown("""
                Selamat datang di analisis **Pertumbuhan Populasi Mahasiswa**! 🌱
                Di sini, Anda dapat menjelajahi bagaimana populasi mahasiswa di universitas yang dipilih telah berkembang selama bertahun-tahun. 
                Visualisasi ini memberikan wawasan tentang tren pendaftaran, mencerminkan aksesibilitas dan popularitas pendidikan tinggi. 📚✨

                **Mengapa Ini Penting?** 🤔
                - **Memahami Tren**: Menganalisis pertumbuhan populasi mahasiswa membantu mengidentifikasi tren dalam pendidikan, seperti permintaan yang meningkat untuk program tertentu atau pergeseran demografi.
                - **Pertumbuhan Institusi**: Populasi mahasiswa yang berkembang sering kali menunjukkan reputasi dan sumber daya universitas yang semakin meningkat.
                - **Perencanaan Masa Depan**: Wawasan tentang tren pendaftaran dapat membantu universitas dalam merencanakan infrastruktur, fakultas, dan sumber daya di masa depan. 🏫

                **Cara Menggunakan Fitur Ini**: 
                1. Pilih universitas dari menu dropdown di bawah.
                2. Amati perubahan populasi mahasiswa dari tahun ke tahun.
                3. Analisis tren dan pertimbangkan apa artinya bagi masa depan pendidikan! 🔍

                Mari kita selami data dan lihat bagaimana populasi mahasiswa telah berubah seiring waktu! 🚀
            """)

            university = st.selectbox("Select a University:", options=data["Name"].unique())
            uni_data = data[data["Name"] == university]

            if not uni_data.empty:
                # Create a line chart for student population growth
                fig = px.line(
                    uni_data,
                    x="Year",
                    y="Student Population",
                    title=f"📊 Pertumbuhan Populasi Mahasiswa untuk {university}",
                    labels={"Student Population": "Jumlah Mahasiswa", "Year": "Tahun"},
                    markers=True
                )
                
                # Add a fill area under the line for better visualization
                fig.add_scatter(
                    x=uni_data["Year"],
                    y=uni_data["Student Population"],
                    fill='tozeroy',
                    mode='none',
                    fillcolor='rgba(0, 100, 200, 0.2)'  # Light blue fill
                )

                # Update layout for better aesthetics
                fig.update_layout(
                    title_x=0,  # Align title to the left
                    title_xanchor='left',  # Anchor the title to the left
                    title_font=dict(size=20),  # Increase title font size
                    xaxis=dict(title='Tahun'),
                    yaxis=dict(title='Jumlah Mahasiswa'),
                    margin=dict(l=40, r=40, t=40, b=40),  # Adjust margins
                    hovermode="x unified"  # Unified hover for better readability
                )

                st.plotly_chart(fig)

                # Key insights section
                st.markdown(f"""
                    **Insight Utama untuk {university}:** 🔑
                    - **Populasi Mahasiswa Saat Ini:** {uni_data['Student Population'].iloc[-1]} di {uni_data['Year'].iloc[-1]}
                    - **Populasi Mahasiswa Tertinggi:** {uni_data['Student Population'].max()} di {uni_data.loc[uni_data['Student Population'].idxmax(), 'Year']}
                    - **Tren Keseluruhan:** {'📈 Meningkat' if uni_data['Student Population'].iloc[-1] > uni_data['Student Population'].iloc[0] else '📉 Menurun'}
                    
                    Tren ini dapat membantu Anda memahami pertumbuhan universitas dan dampaknya terhadap lanskap pendidikan. 🌍
                """)

                # Additional insights or recommendations
                st.markdown("""
                    **Apa Artinya Ini?** 💡
                    - Peningkatan konsisten dalam populasi mahasiswa dapat menunjukkan reputasi yang kuat dan permintaan untuk program-program.
                    - Penurunan dapat menunjukkan perlunya universitas untuk menyesuaikan tawaran mereka atau meningkatkan kepuasan mahasiswa.
                    - Pertimbangkan bagaimana tren ini dapat mempengaruhi pasar kerja di masa depan dan kebijakan pendidikan! 📈
                """)
            else:
                st.warning("Tidak ada data tersedia untuk universitas yang dipilih.")

        # Comparison Between University
        elif choice == "Comparison Between University":
            st.subheader("🏫 Comparison Between Universities")
            st.markdown("""
                Visualisasi ini menampilkan perbandingan universitas yang dipilih berdasarkan **Teaching**, **Research Environment** dan **Research Quality**. 📊✨
                
                **Mengapa Ini Penting?** 🤔
                - **Memahami Kekuatan**: Perbandingan ini membantu Anda memahami kekuatan dan kelemahan masing-masing universitas.
                - **Pengambilan Keputusan**: Data ini dapat membantu calon mahasiswa dalam memilih universitas yang sesuai dengan kebutuhan mereka.
                - **Analisis Kebijakan**: Universitas dapat menggunakan data ini untuk merumuskan strategi peningkatan kualitas pendidikan. 📈
            """)

            # Pilih universitas pertama
            university_population1 = st.selectbox("Select the First University:", options=data["Name"].unique())
            population_data1 = data[data["Name"] == university_population1]

            # Pilih universitas kedua
            university_population2 = st.selectbox("Select the Second University:", options=data["Name"].unique())
            population_data2 = data[data["Name"] == university_population2]

            # Menggabungkan data untuk visualisasi
            comparison_data = pd.DataFrame({
                'University': [university_population1, university_population2],
                'Teaching': [population_data1['Teaching'].values[0], population_data2['Teaching'].values[0]],
                'Research Environment': [population_data1['Research Environment'].values[0], population_data2['Research Environment'].values[0]],
                'Research Quality': [population_data1['Research Quality'].values[0], population_data2['Research Quality'].values[0]]
            })

            # Mengubah DataFrame ke format panjang untuk visualisasi
            comparison_data_long = comparison_data.melt(id_vars='University', 
                                                        value_vars=['Teaching', 'Research Environment', 'Research Quality'],
                                                        var_name='Metrics', 
                                                        value_name='Score')

            # Visualisasi perbandingan
            fig = px.bar(comparison_data_long, 
                        x='University', 
                        y='Score', 
                        color='Metrics', 
                        title=f"📊 Perbandingan: {university_population1} VS {university_population2}",
                        labels={"Score": "Score", "Metrics": "Metrics"},
                        barmode='group',
                        color_discrete_sequence=px.colors.qualitative.Set2)  # Use a qualitative color palette

            # Menambahkan anotasi untuk meningkatkan pemahaman
            fig.update_layout(
                title_x=0,  # Align title to the left
                title_xanchor='left',  # Anchor the title to the left
                title_font=dict(size=16),  # Decrease title font size
                xaxis=dict(title='Universities'),
                yaxis=dict(title='Score'),
                margin=dict(l=40, r=40, t=40, b=40)  # Adjust margins
            )

            # Menampilkan grafik
            st.plotly_chart(fig)

            # Key insights section
            st.markdown("""
                **Insight Utama**: 🔑
                - Perbandingan ini memberikan gambaran jelas tentang kekuatan masing-masing universitas dalam hal pengajaran dan penelitian.
                - Amati metrik mana yang lebih tinggi dan pertimbangkan faktor-faktor lain yang mungkin mempengaruhi keputusan Anda.
                - Data ini dapat membantu dalam merumuskan strategi untuk meningkatkan kualitas pendidikan di masing-masing universitas. 📚
            """)



