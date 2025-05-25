# NewsBuddies 📰

**News For Kids** - A Flutter app that transforms complex news articles into child-friendly content using AI.

![Flutter](https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white)
![Dart](https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white)
![AI](https://img.shields.io/badge/AI_Powered-FF6B6B?style=for-the-badge&logo=openai&logoColor=white)

## 🌟 What is NewsBuddies?

NewsBuddies is an innovative mobile application designed to make news accessible and educational for children aged 3-18. The app fetches real-time news articles and uses AI to transform complex content into age-appropriate, engaging summaries that kids can easily understand.

### Key Features

- **Age-Appropriate Content**: Automatically adapts news summaries based on the child's age
- **Interactive Q&A**: Kids can ask questions about stories and get child-friendly explanations
- **Parental Dashboard**: Parents can monitor their child's reading activity and engagement
- **Real-Time News**: Fetches latest news from reliable sources
- **Smart Content Processing**: Uses web scraping to get full article content when available
- **Child-Friendly UI**: Colorful, intuitive interface designed specifically for young users

## 🏗️ How It Works

### News Processing Pipeline

1. **News Fetching**: Retrieves latest headlines from NewsAPI
2. **Content Scraping**: Attempts to scrape full article content from source URLs
3. **AI Summarization**: Uses Ollama's Llama 3.2 model to create age-appropriate summaries
4. **Interactive Features**: Enables Q&A functionality for deeper learning

### App Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Kids Zone     │    │  Parent Zone    │    │   AI Backend    │
│                 │    │                 │    │                 │
│ • Story Cards   │    │ • Login Screen  │    │ • Ollama/Llama  │
│ • Q&A Feature   │◄──►│ • Activity Log  │◄──►│ • Summarization │
│ • Like Stories  │    │ • Statistics    │    │ • Q&A Responses │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                        │                        │
         └────────────────────────┼────────────────────────┘
                                  │
                    ┌─────────────▼─────────────┐
                    │      NewsAPI Service      │
                    │                           │
                    │ • Headlines Fetching      │
                    │ • Article Metadata        │
                    └───────────────────────────┘
```

## 🛠️ Technologies Used

### Frontend Framework
- **Flutter 3.x**: Cross-platform mobile development framework
- **Dart**: Programming language for Flutter development

### State Management
- **StatefulWidget**: Built-in Flutter state management for component state
- **setState()**: For reactive UI updates

### Backend & AI
- **Ollama**: Local AI inference server
- **Llama 3.2**: Large language model for text summarization and Q&A
- **NewsAPI**: Real-time news data provider

### HTTP & Data Processing
- **http package**: For API calls and web requests
- **html package**: For web scraping and HTML parsing
- **dart:convert**: JSON parsing and data serialization

### UI Components
- **Material Design**: Google's design system implementation
- **Custom gradients and animations**: Enhanced visual appeal
- **Responsive layouts**: Adaptive UI for different screen sizes

## 📱 App Structure

### Main Components

#### 1. **NewsBuddiesApp** (Root Widget)
- App configuration and theming
- Material Design setup
- Navigation structure

#### 2. **MainScreen** (Navigation Hub)
- Bottom navigation between Kids and Parent zones
- Shared state management for articles and activities
- Activity tracking coordination

#### 3. **KidsDashboard** (Kids Zone)
- Age input and personalization
- News article grid display
- Article loading and processing
- Child-friendly interface design

#### 4. **ArticleDetailScreen** (Story Reader)
- Full story display with enhanced typography
- Interactive Q&A functionality
- Like/favorite system
- AI-powered question answering

#### 5. **ParentLoginScreen** (Parent Zone)
- Password-protected access (`parent123`)
- Reading activity monitoring
- Statistics dashboard
- Child engagement metrics

### Data Models

```dart
class ArticleSummary {
  final String title;           // Article headline
  final String summary;         // AI-generated child summary
  final String url;            // Original article URL
  final String fullContent;    // Scraped full text
  final bool wasScraped;       // Content scraping success flag
}

class ReadingActivity {
  final String articleTitle;   // Tracked article
  final String action;         // 'opened', 'liked', etc.
  final DateTime timestamp;    // Activity time
}

class QAMessage {
  final String question;       // Child's question
  final String answer;         // AI-generated answer
}
```

## 🔧 Setup & Installation

### Prerequisites

1. **Flutter SDK** (3.0 or higher)
2. **Dart SDK** (3.0 or higher)
3. **Ollama** server running locally
4. **NewsAPI** account and API key

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd newsbuddies
   ```

2. **Install dependencies**
   ```bash
   flutter pub get
   ```

3. **Set up Ollama**
   ```bash
   # Install Ollama
   curl -fsSL https://ollama.ai/install.sh | sh
   
   # Pull Llama 3.2 model
   ollama pull llama3.2
   
   # Start Ollama server
   ollama serve
   ```

4. **Configure API keys**
   - Replace `newsApiKey` in the code with your NewsAPI key
   - Update `ollamaBaseUrl` if needed (default: `http://10.0.2.2:11434`)

5. **Run the app**
   ```bash
   flutter run
   ```

## 🔑 Configuration

### API Keys & Endpoints

```dart
// NewsAPI configuration
final String _newsApiKey = "YOUR_NEWSAPI_KEY_HERE";

// Ollama configuration  
final String _ollamaBaseUrl = "http://10.0.2.2:11434"; // Android emulator
// Use "http://localhost:11434" for iOS simulator
```

### Parent Access

- **Default Password**: `parent123`
- Modify in `ParentLoginScreen._login()` method

## 🎯 Features Breakdown

### For Kids
- **Personalized Experience**: Content adapted to child's age
- **Visual Learning**: Card-based story presentation
- **Interactive Elements**: Tap to read, like stories, ask questions
- **Safe Environment**: No external links or inappropriate content

### For Parents
- **Activity Monitoring**: Track what stories kids read and like
- **Engagement Metrics**: See reading patterns and preferences
- **Secure Access**: Password-protected dashboard
- **Real-time Updates**: Live activity feed

### AI Integration
- **Smart Summarization**: Complex news → child-friendly summaries
- **Contextual Q&A**: Answer questions about specific stories
- **Age Adaptation**: Content complexity matches child's age
- **Educational Focus**: Emphasizes learning and understanding

## 🚀 Technical Highlights

### Advanced Features

1. **Intelligent Content Scraping**
   - Multiple CSS selector strategies
   - Fallback to API content when scraping fails
   - Content quality validation

2. **Robust Error Handling**
   - Network connectivity checks
   - API failure graceful degradation
   - User-friendly error messages

3. **Performance Optimization**
   - Lazy loading of articles
   - Efficient state management
   - Minimal API calls

4. **Responsive Design**
   - Adaptive layouts for different screen sizes
   - Consistent visual hierarchy
   - Accessibility considerations

## 🎨 Design Philosophy

- **Child-Centric**: Every design decision prioritizes young users
- **Safety First**: No external navigation or inappropriate content
- **Educational**: Encourages learning through interaction
- **Parental Control**: Transparent activity monitoring
- **Modern UI**: Contemporary design with engaging animations

## 🔍 Future Enhancements

- Voice narration for younger children
- Offline reading capability
- Multiple language support
- Educational quizzes and games
- Social features (with parental controls)
- Advanced analytics for parents


## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

**NewsBuddies** - Making news accessible, educational, and fun for the next generation! 🌟
