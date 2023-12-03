import cv2

def play_video(file_path):
    # Buka file video
    cap = cv2.VideoCapture(file_path)

    # Periksa apakah file video berhasil dibuka
    if not cap.isOpened():
        print("Error: Gagal membuka file video.")
        return

    while True:
        # Baca frame dari video
        ret, frame = cap.read()

        # Periksa apakah bacaan frame berhasil
        if not ret:
            print("Error: Gagal membaca frame dari video.")
            break

        # Tampilkan frame
        cv2.imshow('Video Player', frame)

        # Hentikan pemutaran jika pengguna menekan tombol 'q'
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    # Tutup video
    cap.release()

    # Tutup jendela tampilan
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = "me.mp4"  # Ganti dengan path file video Anda
    play_video(video_path)
