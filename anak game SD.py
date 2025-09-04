<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Game Matematika untuk Anak SD</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Comic Sans MS', 'Arial', sans-serif;
        }
        
        body {
            background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .container {
            background-color: white;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            width: 100%;
            max-width: 500px;
            padding: 30px;
            text-align: center;
        }
        
        h1 {
            color: #ff6d00;
            font-size: 2.5rem;
            margin-bottom: 20px;
            text-shadow: 2px 2px 0px #ffab00;
        }
        
        .game-area {
            margin: 30px 0;
        }
        
        .score {
            font-size: 1.5rem;
            color: #5d4037;
            margin-bottom: 20px;
        }
        
        .question {
            font-size: 3rem;
            color: #ff6d00;
            margin: 20px 0;
            font-weight: bold;
        }
        
        .answer-input {
            width: 150px;
            height: 70px;
            font-size: 2rem;
            text-align: center;
            border: 3px solid #ffab00;
            border-radius: 10px;
            margin: 20px auto;
            display: block;
        }
        
        .btn {
            background-color: #ffab00;
            color: white;
            border: none;
            border-radius: 50px;
            padding: 15px 30px;
            font-size: 1.2rem;
            cursor: pointer;
            margin: 10px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        
        .btn:hover {
            background-color: #ff6d00;
            transform: translateY(-3px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
        }
        
        .grade-selection {
            margin: 20px 0;
        }
        
        .grade-btn {
            background-color: #64b5f6;
            margin: 5px;
            padding: 10px 20px;
        }
        
        .grade-btn:hover {
            background-color: #1976d2;
        }
        
        .grade-btn.active {
            background-color: #1976d2;
            transform: scale(1.1);
        }
        
        .feedback {
            font-size: 1.5rem;
            margin: 20px 0;
            height: 40px;
            font-weight: bold;
        }
        
        .correct {
            color: #4caf50;
        }
        
        .incorrect {
            color: #f44336;
        }
        
        .profile {
            text-align: left;
            margin: 20px 0;
            padding: 15px;
            background-color: #fff8e1;
            border-radius: 10px;
        }
        
        .profile h2 {
            color: #ff6d00;
            margin-bottom: 15px;
            text-align: center;
        }
        
        .profile-item {
            margin: 10px 0;
            font-size: 1.2rem;
        }
        
        .profile-input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 2px solid #ffab00;
            border-radius: 5px;
            font-size: 1rem;
        }
        
        .tabs {
            display: flex;
            margin-bottom: 20px;
        }
        
        .tab {
            flex: 1;
            padding: 10px;
            background-color: #ffcc80;
            cursor: pointer;
            border-radius: 10px 10px 0 0;
            margin-right: 5px;
        }
        
        .tab.active {
            background-color: #ff6d00;
            color: white;
        }
        
        .tab-content {
            display: none;
        }
        
        .tab-content.active {
            display: block;
        }
        
        .math-characters {
            position: absolute;
            font-size: 2rem;
            opacity: 0.1;
            color: #ff6d00;
            z-index: -1;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Game Matematika</h1>
        
        <div class="tabs">
            <div class="tab active" onclick="showTab('game')">Game</div>
            <div class="tab" onclick="showTab('profile')">Profil</div>
        </div>
        
        <div id="game-tab" class="tab-content active">
            <div class="game-area">
                <div class="score">Skor: <span id="score">0</span></div>
                
                <div class="grade-selection">
                    <p>Pilih Kelas:</p>
                    <button class="btn grade-btn active" onclick="selectGrade(1)">Kelas 1</button>
                    <button class="btn grade-btn" onclick="selectGrade(2)">Kelas 2</button>
                    <button class="btn grade-btn" onclick="selectGrade(3)">Kelas 3</button>
                    <button class="btn grade-btn" onclick="selectGrade(4)">Kelas 4</button>
                    <button class="btn grade-btn" onclick="selectGrade(5)">Kelas 5</button>
                    <button class="btn grade-btn" onclick="selectGrade(6)">Kelas 6</button>
                </div>
                
                <div class="question" id="question">5 + 3 = ?</div>
                
                <input type="number" class="answer-input" id="answer" placeholder="Jawab">
                
                <button class="btn" onclick="checkAnswer()">Jawab</button>
                
                <div class="feedback" id="feedback"></div>
            </div>
        </div>
        
        <div id="profile-tab" class="tab-content">
            <div class="profile">
                <h2>Profil Pengguna</h2>
                
                <div class="profile-item">
                    <label for="player-name">Nama:</label>
                    <input type="text" id="player-name" class="profile-input" placeholder="Masukkan nama">
                </div>
                
                <div class="profile-item">
                    <label for="high-score">Skor Tertinggi:</label>
                    <div id="high-score">0</div>
                </div>
                
                <div class="profile-item">
                    <label for="current-level">Level Saat Ini:</label>
                    <div id="current-level">Kelas 1</div>
                </div>
                
                <button class="btn" onclick="saveProfile()">Simpan Profil</button>
            </div>
        </div>
    </div>
    
    <script>
        // Variabel global
        let score = 0;
        let highScore = localStorage.getItem('mathGameHighScore') || 0;
        let currentGrade = 1;
        let playerName = localStorage.getItem('mathGamePlayerName') || '';
        let currentAnswer = 0;
        
        // Inisialisasi
        document.addEventListener('DOMContentLoaded', function() {
            document.getElementById('high-score').textContent = highScore;
            document.getElementById('player-name').value = playerName;
            generateNewQuestion();
            
            // Fokus ke input jawaban saat menekan enter
            document.getElementById('answer').addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    checkAnswer();
                }
            });
        });
        
        // Fungsi untuk menampilkan tab
        function showTab(tabName) {
            // Sembunyikan semua tab
            document.querySelectorAll('.tab-content').forEach(tab => {
                tab.classList.remove('active');
            });
            
            // Hapus kelas active dari semua tombol tab
            document.querySelectorAll('.tab').forEach(tabBtn => {
                tabBtn.classList.remove('active');
            });
            
            // Tampilkan tab yang dipilih
            document.getElementById(tabName + '-tab').classList.add('active');
            
            // Tambahkan kelas active ke tombol tab yang dipilih
            event.target.classList.add('active');
        }
        
        // Fungsi untuk memilih kelas
        function selectGrade(grade) {
            currentGrade = grade;
            
            // Update UI
            document.querySelectorAll('.grade-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            event.target.classList.add('active');
            
            // Update di profil
            document.getElementById('current-level').textContent = `Kelas ${grade}`;
            
            // Generate soal baru
            generateNewQuestion();
        }
        
        // Fungsi untuk generate soal baru
        function generateNewQuestion() {
            const random = Math.random();
            let num1, num2, operator, questionText;
            
            // Reset feedback
            document.getElementById('feedback').textContent = '';
            document.getElementById('feedback').className = 'feedback';
            
            // Generate soal berdasarkan kelas
            switch(currentGrade) {
                case 1:
                    // Kelas 1: Penjumlahan sederhana (1-10)
                    num1 = Math.floor(Math.random() * 10) + 1;
                    num2 = Math.floor(Math.random() * 10) + 1;
                    operator = '+';
                    currentAnswer = num1 + num2;
                    break;
                    
                case 2:
                    // Kelas 2: Penjumlahan dan pengurangan (1-20)
                    num1 = Math.floor(Math.random() * 20) + 1;
                    num2 = Math.floor(Math.random() * 20) + 1;
                    if (random < 0.5) {
                        operator = '+';
                        currentAnswer = num1 + num2;
                    } else {
                        operator = '-';
                        // Pastikan hasilnya tidak negatif
                        if (num1 < num2) {
                            [num1, num2] = [num2, num1];
                        }
                        currentAnswer = num1 - num2;
                    }
                    break;
                    
                case 3:
                    // Kelas 3: Perkalian sederhana (1-10)
                    num1 = Math.floor(Math.random() * 10) + 1;
                    num2 = Math.floor(Math.random() * 10) + 1;
                    operator = '×';
                    currentAnswer = num1 * num2;
                    break;
                    
                case 4:
                    // Kelas 4: Pembagian sederhana
                    num2 = Math.floor(Math.random() * 8) + 2; // Pembagi 2-9
                    currentAnswer = Math.floor(Math.random() * 10) + 1; // Hasil 1-10
                    num1 = num2 * currentAnswer; // Dividen
                    operator = '÷';
                    break;
                    
                case 5:
                    // Kelas 5: Operasi campuran
                    num1 = Math.floor(Math.random() * 15) + 1;
                    num2 = Math.floor(Math.random() * 15) + 1;
                    const ops = ['+', '-', '×'];
                    operator = ops[Math.floor(Math.random() * ops.length)];
                    
                    if (operator === '+') {
                        currentAnswer = num1 + num2;
                    } else if (operator === '-') {
                        if (num1 < num2) {
                            [num1, num2] = [num2, num1];
                        }
                        currentAnswer = num1 - num2;
                    } else {
                        currentAnswer = num1 * num2;
                    }
                    break;
                    
                case 6:
                    // Kelas 6: Operasi lebih kompleks
                    num1 = Math.floor(Math.random() * 20) + 1;
                    num2 = Math.floor(Math.random() * 20) + 1;
                    const ops6 = ['+', '-', '×', '÷'];
                    operator = ops6[Math.floor(Math.random() * ops6.length)];
                    
                    if (operator === '+') {
                        currentAnswer = num1 + num2;
                    } else if (operator === '-') {
                        if (num1 < num2) {
                            [num1, num2] = [num2, num1];
                        }
                        currentAnswer = num1 - num2;
                    } else if (operator === '×') {
                        currentAnswer = num1 * num2;
                    } else {
                        // Pembagian dengan hasil bulat
                        if (num1 < num2) {
                            [num1, num2] = [num2, num1];
                        }
                        currentAnswer = Math.floor(num1 / num2);
                        num1 = num2 * currentAnswer;
                    }
                    break;
            }
            
            // Tampilkan soal
            questionText = `${num1} ${operator} ${num2} = ?`;
            document.getElementById('question').textContent = questionText;
            
            // Kosongkan input jawaban dan fokus
            document.getElementById('answer').value = '';
            document.getElementById('answer').focus();
        }
        
        // Fungsi untuk mengecek jawaban
        function checkAnswer() {
            const userAnswer = parseInt(document.getElementById('answer').value);
            const feedbackElement = document.getElementById('feedback');
            
            if (isNaN(userAnswer)) {
                feedbackElement.textContent = 'Masukkan jawaban yang valid!';
                feedbackElement.className = 'feedback incorrect';
                return;
            }
            
            if (userAnswer === currentAnswer) {
                // Jawaban benar
                score += currentGrade * 10; // Skor berdasarkan tingkat kesulitan
                document.getElementById('score').textContent = score;
                
                feedbackElement.textContent = 'Benar! 🎉';
                feedbackElement.className = 'feedback correct';
                
                // Cek apakah skor melebihi high score
                if (score > highScore) {
                    highScore = score;
                    localStorage.setItem('mathGameHighScore', highScore);
                    document.getElementById('high-score').textContent = highScore;
                }
                
                // Generate soal baru setelah 1 detik
                setTimeout(generateNewQuestion, 1000);
            } else {
                // Jawaban salah
                feedbackElement.textContent = `Salah! Jawaban: ${currentAnswer}`;
                feedbackElement.className = 'feedback incorrect';
                
                // Generate soal baru setelah 2 detik
                setTimeout(generateNewQuestion, 2000);
            }
        }
        
        // Fungsi untuk menyimpan profil
        function saveProfile() {
            playerName = document.getElementById('player-name').value;
            localStorage.setItem('mathGamePlayerName', playerName);
            
            // Tampilkan notifikasi
            const feedbackElement = document.getElementById('feedback');
            feedbackElement.textContent = 'Profil berhasil disimpan!';
            feedbackElement.className = 'feedback correct';
            
            // Sembunyikan notifikasi setelah 2 detik
            setTimeout(() => {
                feedbackElement.textContent = '';
                feedbackElement.className = 'feedback';
            }, 2000);
        }
    </script>
</body>
</html>