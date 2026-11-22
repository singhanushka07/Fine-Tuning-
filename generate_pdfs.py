"""Generate 3 detailed PDFs for the PEFT Platform project."""
import os
from fpdf import FPDF

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))


class StyledPDF(FPDF):
    """Base PDF with consistent styling."""

    def __init__(self, title, subtitle):
        super().__init__()
        self._title = title
        self._subtitle = subtitle
        self.set_auto_page_break(auto=True, margin=20)

    def header(self):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 8, self._title, align="R", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(99, 102, 241)
        self.set_line_width(0.5)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"PEFT QLoRA Fine-Tuning Platform  |  Page {self.page_no()}/{{nb}}", align="C")

    def add_cover(self):
        self.add_page()
        self.ln(50)
        self.set_font("Helvetica", "B", 28)
        self.set_text_color(99, 102, 241)
        self.set_x(10)
        self.multi_cell(190, 12, self._title, align="C")
        self.ln(6)
        self.set_font("Helvetica", "", 13)
        self.set_text_color(100, 100, 100)
        self.set_x(10)
        self.multi_cell(190, 8, self._subtitle, align="C")
        self.ln(20)
        self.set_font("Helvetica", "", 11)
        self.set_text_color(60, 60, 60)
        self.set_x(10)
        self.multi_cell(190, 7, "Project: PEFT QLoRA Fine-Tuning Platform for Llama 3 8B", align="C")
        self.set_x(10)
        self.multi_cell(190, 7, "Domain-Specific Adaptation with 4-bit Quantization & LoRA Adapters", align="C")
        self.ln(30)
        self.set_draw_color(99, 102, 241)
        self.set_line_width(1)
        self.line(60, self.get_y(), 150, self.get_y())

    def section_title(self, num, title):
        self.ln(6)
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(99, 102, 241)
        label = f"{num}. {title}" if num else title
        self.cell(0, 10, label, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(99, 102, 241)
        self.set_line_width(0.3)
        self.line(10, self.get_y(), 120, self.get_y())
        self.ln(4)

    def sub_title(self, title):
        self.ln(3)
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(59, 130, 246)
        self.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def body_text(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(40, 40, 40)
        self.multi_cell(0, 6, text)
        self.ln(2)

    def bullet(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(40, 40, 40)
        x = self.get_x()
        self.cell(6, 6, chr(8226))
        self.multi_cell(0, 6, text)
        self.ln(1)

    def key_value(self, key, value):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(50, 50, 50)
        self.cell(50, 6, key + ":")
        self.set_font("Helvetica", "", 10)
        self.set_text_color(40, 40, 40)
        self.multi_cell(0, 6, value)
        self.ln(1)

    def question_block(self, num, question, answer):
        self.ln(3)
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(99, 102, 241)
        self.multi_cell(0, 7, f"Q{num}: {question}")
        self.ln(1)
        self.set_font("Helvetica", "", 10)
        self.set_text_color(40, 40, 40)
        self.multi_cell(0, 6, f"Answer: {answer}")
        self.ln(2)
        self.set_draw_color(220, 220, 220)
        self.set_line_width(0.2)
        self.line(10, self.get_y(), 200, self.get_y())


# ============================================================
# PDF 1: TECH STACK
# ============================================================
def generate_tech_stack_pdf():
    pdf = StyledPDF(
        "Tech Stack & Architecture",
        "Complete Technology Breakdown with Rationale for Every Choice"
    )
    pdf.alias_nb_pages()
    pdf.add_cover()

    # --- OVERVIEW ---
    pdf.add_page()
    pdf.section_title(1, "Project Overview")
    pdf.body_text(
        "The PEFT (Parameter-Efficient Fine-Tuning) Platform is a full-stack web application "
        "that showcases mastery of QLoRA fine-tuning for Meta's Llama 3 8B model. It demonstrates "
        "how domain-specific language models can be created using only 0.085% of the original parameters, "
        "achieving 99.9% parameter reduction and 75% memory savings compared to full fine-tuning. "
        "The platform features a production-grade UI with dark/light themes, glassmorphism design, "
        "animated data visualizations, a simulated inference playground, and an interactive architecture "
        "explainer -- all backed by a FastAPI service with a 3-tier fallback system."
    )

    # --- FRONTEND FRAMEWORK ---
    pdf.section_title(2, "Frontend Technologies")

    pdf.sub_title("Next.js 13.4 (App Router)")
    pdf.key_value("What", "React meta-framework by Vercel with server-side rendering, file-based routing, and built-in optimizations")
    pdf.key_value("Version", "13.4.19 -- stable App Router release before the major v14/v15 rewrites")
    pdf.body_text(
        "Why chosen: Next.js provides the App Router architecture which enables a clear separation between "
        "server and client components. The file-system based routing (app/ directory) eliminates manual route "
        "configuration. Built-in features like automatic code splitting, image optimization, and font optimization "
        "(next/font) reduce bundle sizes without manual webpack config. Server-side rendering ensures fast initial "
        "page loads and proper SEO -- important for a portfolio/showcase project."
    )
    pdf.body_text(
        "Alternatives considered: (1) Create React App -- deprecated, no SSR, no file-based routing. "
        "(2) Vite + React -- faster dev server but no SSR out of the box, requires manual routing setup. "
        "(3) Remix -- excellent nested routing but smaller ecosystem, less community content for portfolios. "
        "(4) Astro -- great for static content but this project needs heavy client interactivity."
    )

    pdf.sub_title("React 18")
    pdf.key_value("What", "Declarative component-based UI library with concurrent rendering features")
    pdf.key_value("Version", "18.2.0 -- latest stable with concurrent features, Suspense, and transitions")
    pdf.body_text(
        "Why chosen: React 18 introduces Concurrent Mode features including Suspense for data fetching, "
        "automatic batching of state updates, and transitions for non-urgent updates. The component model "
        "makes it natural to build reusable UI pieces (GlassCard, AnimatedCounter, SkeletonLoader) that "
        "compose into complex pages. The vast ecosystem means every visualization library, animation library, "
        "and state manager supports React first-class."
    )

    pdf.sub_title("TypeScript 4.9")
    pdf.key_value("What", "Typed superset of JavaScript that compiles to plain JS")
    pdf.body_text(
        "Why chosen: TypeScript catches entire categories of bugs at compile time -- wrong prop types, "
        "missing fields, null dereferences. In a project with complex data shapes (training metrics with "
        "nested arrays, model config objects, inference responses with multiple fields), TypeScript provides "
        "living documentation. It also enables superior IDE support with autocomplete, go-to-definition, "
        "and inline error reporting. For a showcase project, TypeScript signals production-grade engineering "
        "practices."
    )

    pdf.sub_title("Tailwind CSS v3")
    pdf.key_value("What", "Utility-first CSS framework that generates only the classes you use")
    pdf.key_value("Version", "3.4.19 -- latest v3 stable, compatible with Next.js 13 PostCSS pipeline")
    pdf.body_text(
        "Why chosen: Tailwind's utility-first approach eliminates CSS naming debates and dead code. "
        "Classes like 'grid grid-cols-3 gap-4 p-6 rounded-xl' are self-documenting and co-located with the "
        "markup. The purge system ensures the production CSS only contains classes actually used, resulting in "
        "tiny bundles (~40KB). Combined with CSS custom properties for the theme system (--bg-primary, "
        "--text-primary, --glass-bg), Tailwind handles layout/spacing while custom properties handle theming. "
        "The 'darkMode: class' configuration works perfectly with the ThemeProvider toggle."
    )
    pdf.body_text(
        "Why v3 not v4: Tailwind v4 uses a new CSS-first configuration (@import 'tailwindcss') that requires "
        "the @tailwindcss/postcss plugin. This is incompatible with Next.js 13's webpack-based PostCSS pipeline. "
        "Tailwind v3 has native Next.js 13 support via the standard PostCSS plugin system."
    )

    pdf.sub_title("Framer Motion")
    pdf.key_value("What", "Production-ready animation library for React with declarative API")
    pdf.body_text(
        "Why chosen: Framer Motion provides the most developer-friendly animation API in the React ecosystem. "
        "Key features used in this project:\n"
        "- motion.div with whileHover, whileTap, whileInView for scroll-triggered reveals\n"
        "- AnimatePresence for mount/unmount animations (theme toggle, mobile menu, fallback banner)\n"
        "- layoutId for shared layout animations (active nav indicator slides between links)\n"
        "- staggerChildren/delayChildren for cascading card entrance animations\n"
        "- animate() imperative API for the AnimatedCounter (spring-physics number counting)\n"
        "- Spring physics for natural-feeling transitions (type: 'spring', stiffness, damping)\n\n"
        "Alternatives considered: (1) CSS animations only -- limited, no spring physics, no layout animations. "
        "(2) React Spring -- similar capability but more verbose API, smaller community. "
        "(3) GSAP -- powerful but imperative, doesn't integrate as naturally with React's declarative model."
    )

    pdf.sub_title("Recharts")
    pdf.key_value("What", "Composable charting library built on D3 with React components")
    pdf.body_text(
        "Why chosen: Recharts wraps D3's powerful data visualization in React components, making charts "
        "composable and declarative. Components like <AreaChart>, <LineChart>, <PieChart>, <BarChart> accept "
        "data arrays and render SVG. Gradient definitions under curves (linearGradient defs), custom tooltips "
        "with glassmorphism styling, and responsive containers are straightforward. Used for training loss curves, "
        "learning rate schedules, gradient norms, epoch progress, memory comparison bars, and latency charts."
    )
    pdf.body_text(
        "Alternatives considered: (1) Chart.js/react-chartjs-2 -- canvas-based, less customizable for themed SVG. "
        "(2) Victory -- similar but larger bundle. (3) D3 directly -- too low-level for this use case. "
        "(4) Nivo -- excellent but heavier, more opinionated styling."
    )

    pdf.sub_title("TanStack Query v5 (React Query)")
    pdf.key_value("What", "Async state management for server data -- caching, refetching, stale-while-revalidate")
    pdf.body_text(
        "Why chosen: TanStack Query elegantly separates server state from client state. The useQuery hook "
        "handles all the complexity of fetching, caching, background refetching, error/loading states, and "
        "stale data management. In this project, hooks like useModelInfo(), useTrainingMetrics(), and "
        "useInference() wrap API calls with automatic retry, configurable stale times, and loading/error "
        "states that feed directly into skeleton loaders. The QueryClient configuration sets global "
        "defaults for retry count, stale time, and refetch intervals."
    )
    pdf.body_text(
        "Alternatives considered: (1) SWR by Vercel -- similar but less features (no mutation tracking, "
        "less devtools). (2) Redux Toolkit Query -- more boilerplate, overkill when you already have Zustand "
        "for client state. (3) Plain useEffect + useState -- error-prone, no caching, duplicated logic."
    )

    pdf.sub_title("Zustand")
    pdf.key_value("What", "Minimal state management library -- 1KB, no boilerplate, no providers")
    pdf.body_text(
        "Why chosen: Zustand provides global client state with zero boilerplate. A store is a single "
        "function that returns state and actions. No Provider wrappers needed (unlike Redux or Context), "
        "no action types, no reducers. Used for UI state like connection status, fallback mode flags, and "
        "app-wide settings. The separation of concerns is clean: TanStack Query for server state, Zustand "
        "for client state, React Context for theme."
    )

    pdf.sub_title("Axios")
    pdf.key_value("What", "Promise-based HTTP client with interceptors and automatic transforms")
    pdf.body_text(
        "Why chosen: Axios provides a cleaner API than fetch() with automatic JSON parsing, request/response "
        "interceptors for error handling, configurable base URLs, and timeout support. The API client (lib/api.ts) "
        "creates an Axios instance with the backend base URL and attaches response interceptors that detect "
        "fallback mode and update the Zustand store accordingly."
    )

    pdf.sub_title("Lucide React")
    pdf.key_value("What", "Beautiful, consistent icon library -- tree-shakeable SVG React components")
    pdf.body_text(
        "Why chosen: Lucide is the maintained community fork of Feather Icons with 1000+ icons. Each icon "
        "is a standalone React component that tree-shakes perfectly -- importing { Sun, Moon, Menu } only "
        "bundles those 3 icons. Used throughout: navigation icons, stat card icons (Brain, Zap, BarChart3, "
        "Layers), theme toggle (Sun/Moon), mobile menu (Menu/X), copy button (Copy/Check), and more."
    )

    # --- BACKEND ---
    pdf.add_page()
    pdf.section_title(3, "Backend Technologies")

    pdf.sub_title("FastAPI (Python)")
    pdf.key_value("What", "Modern, high-performance Python web framework with automatic API docs")
    pdf.body_text(
        "Why chosen: FastAPI is the ideal backend for ML/AI projects because:\n"
        "- Native async/await support for non-blocking HuggingFace API calls\n"
        "- Automatic OpenAPI (Swagger) documentation at /docs\n"
        "- Pydantic models for request/response validation with type safety\n"
        "- Python ecosystem gives direct access to HuggingFace transformers, datasets, and inference APIs\n"
        "- Built on Starlette for high performance (comparable to Node.js/Go)\n"
        "- Router system for clean API organization (/api/model, /api/metrics, /api/inference)\n\n"
        "Alternatives considered: (1) Flask -- no async, no auto-docs, more boilerplate. "
        "(2) Django REST -- too heavy for an API-only service. "
        "(3) Express.js -- would need Python subprocess for HF calls, unnecessary complexity."
    )

    pdf.sub_title("HuggingFace Inference API")
    pdf.key_value("What", "Hosted inference endpoints for running ML models without local GPU")
    pdf.body_text(
        "Why chosen: The HuggingFace Inference API allows the project to run inference on Llama 3 8B "
        "(both base and fine-tuned) without requiring a local GPU or expensive cloud compute. The API "
        "accepts a prompt and model ID, returning generated text. This project wraps it in a 3-tier "
        "fallback system: Live API -> Cached responses -> Static mock data, ensuring the playground "
        "always works even without an active HF model deployment."
    )

    pdf.sub_title("Uvicorn")
    pdf.key_value("What", "Lightning-fast ASGI server for Python async frameworks")
    pdf.body_text(
        "Why chosen: Uvicorn is the standard ASGI server for FastAPI. It handles the async event loop, "
        "HTTP parsing, and connection management. In development, it provides hot-reload (--reload flag). "
        "In production, it can be paired with Gunicorn for multi-process deployment."
    )

    # --- ARCHITECTURE PATTERNS ---
    pdf.add_page()
    pdf.section_title(4, "Architecture Patterns & Design Decisions")

    pdf.sub_title("CSS Custom Properties Theme System")
    pdf.body_text(
        "The entire theme system is built on CSS custom properties (variables) rather than Tailwind's "
        "built-in dark mode utilities. This provides several advantages:\n"
        "- Single source of truth: :root defines light, .dark overrides for dark mode\n"
        "- Runtime switchable: JavaScript toggles the .dark class, CSS instantly updates\n"
        "- Glassmorphism tokens: --glass-bg, --glass-border, --glass-blur adapt to theme\n"
        "- Chart theming: --chart-grid, --chart-text, --chart-tooltip-bg for Recharts\n"
        "- Smooth transitions: a global CSS transition on background-color/color/border-color\n"
        "- Framework agnostic: the variables work in inline styles, Tailwind classes, and CSS-in-JS"
    )

    pdf.sub_title("3-Tier Fallback Architecture")
    pdf.body_text(
        "The backend implements a robust fallback system ensuring the app always works:\n\n"
        "Tier 1 - Live API: Calls the HuggingFace Inference API with the deployed model ID. "
        "If the model is deployed and the API key is valid, real inference results are returned.\n\n"
        "Tier 2 - Cached Responses: If the live API fails (model not deployed, rate limited, etc.), "
        "the system checks a response cache for previously successful calls with similar prompts.\n\n"
        "Tier 3 - Static Mock Data: If no cache hit, keyword-matching selects a realistic mock response "
        "from MOCK_RESPONSE_PAIRS in fallback_data.py. Each pair has distinct base vs fine-tuned responses "
        "covering topics like capitals, quantum computing, ML vs DL, photosynthesis, and PEFT itself.\n\n"
        "Every API response includes a 'fallback: true/false' flag so the frontend can show the "
        "'Demo Mode Active' banner. Simulated delays (0.8-1.5s) make mock responses feel realistic."
    )

    pdf.sub_title("Component Architecture")
    pdf.body_text(
        "The frontend follows a layered component architecture:\n\n"
        "Layout Layer: ThemeProvider (context), Navbar (navigation + theme toggle), ConnectionStatus, "
        "Providers (QueryClientProvider + ThemeProvider wrapper)\n\n"
        "Shared Layer: GlassCard (reusable glassmorphism container), AnimatedCounter (spring-animated "
        "numbers), SkeletonLoader (shimmer loading states), ConnectionBadge, FallbackBanner\n\n"
        "Feature Layer: StatsCard (dashboard stat cards), TrainingChart (configurable Recharts wrapper), "
        "InferencePanel (typing animation response panel)\n\n"
        "Page Layer: Dashboard (/), Metrics (/metrics), Playground (/playground), Architecture (/architecture)\n\n"
        "Each layer only imports from its own level or below, never upward. This prevents circular "
        "dependencies and makes the component tree predictable."
    )

    pdf.sub_title("Glassmorphism Design System")
    pdf.body_text(
        "Glassmorphism is a design trend using frosted-glass effects:\n"
        "- Semi-transparent backgrounds (rgba with alpha < 1)\n"
        "- backdrop-filter: blur() for the frosted glass effect\n"
        "- Subtle borders with low opacity\n"
        "- Layered shadows for depth\n\n"
        "Implementation: The .glass utility class in globals.css combines --glass-bg, --glass-border, "
        "--glass-blur, and --glass-shadow variables. The GlassCard component wraps any content in a "
        "motion.div with glass styling plus optional hover animation (y: -2, shadow elevation). "
        "Theme-aware: light mode uses white-tinted glass, dark mode uses dark slate-tinted glass."
    )

    pdf.sub_title("Animation Strategy")
    pdf.body_text(
        "Animations serve specific UX purposes, not just decoration:\n\n"
        "1. Entrance animations (staggerChildren): Stats cards appear one-by-one on page load, "
        "giving the user's eye a natural reading path\n\n"
        "2. Scroll-triggered reveals (whileInView): Charts and info sections animate in only when "
        "scrolled into view, improving perceived performance\n\n"
        "3. Typing simulation: The inference playground reveals text character-by-character at different "
        "speeds (base: 20ms/char, finetuned: 12ms/char), demonstrating the speed advantage of fine-tuning\n\n"
        "4. Micro-interactions: Hover effects on cards (y: -2, shadow), nav indicator sliding (layoutId), "
        "theme toggle rotation -- these signal interactivity and polish\n\n"
        "5. Loading states: Shimmer skeletons instead of spinners, maintaining layout stability during loads"
    )

    pdf.sub_title("State Management Architecture")
    pdf.body_text(
        "Three-layer state management, each handling a different concern:\n\n"
        "1. TanStack Query (Server State): All API data -- model info, training metrics, inference results. "
        "Handles caching, background refetching, optimistic updates, and loading/error states. Configured "
        "with staleTime and refetchInterval per query.\n\n"
        "2. Zustand (Client State): App-wide UI state -- connection status, fallback mode, global settings. "
        "No provider needed, direct import and use.\n\n"
        "3. React Context (Theme): Theme state (dark/light) via ThemeProvider. Persisted to localStorage. "
        "Separate from Zustand because it needs to wrap the entire component tree and affect the HTML element."
    )

    # --- DEV TOOLING ---
    pdf.add_page()
    pdf.section_title(5, "Development Tooling & Infrastructure")

    pdf.sub_title("PostCSS + Autoprefixer")
    pdf.body_text(
        "PostCSS processes the CSS pipeline: Tailwind generates utility classes, Autoprefixer adds vendor "
        "prefixes (-webkit-backdrop-filter for Safari glassmorphism support). The postcss.config.js "
        "configures both plugins in order."
    )

    pdf.sub_title("next/font (Inter + JetBrains Mono)")
    pdf.body_text(
        "Next.js 13's built-in font optimization downloads and self-hosts Google Fonts at build time, "
        "eliminating layout shift and external network requests. Inter is the primary sans-serif font "
        "(clean, modern, excellent readability). JetBrains Mono is used for code/monospace contexts "
        "(model IDs, technical values, inference output)."
    )

    pdf.sub_title("Docker Compose")
    pdf.body_text(
        "docker-compose.yml orchestrates the full stack: frontend (Node.js), backend (Python/FastAPI). "
        "Environment variables for HuggingFace API keys and model IDs are configured via .env files. "
        "This enables one-command deployment: 'docker-compose up' starts everything."
    )

    pdf.sub_title("Environment Variables & Configuration")
    pdf.body_text(
        "Sensitive config is managed via environment variables:\n"
        "- HUGGINGFACE_API_KEY: Authentication for HF Inference API\n"
        "- HF_BASE_MODEL_ID: meta-llama/Meta-Llama-3-8B-Instruct\n"
        "- HF_FINETUNED_MODEL_ID: your-username/llama3-8b-finetuned\n"
        "- NEXT_PUBLIC_API_URL: Backend URL for frontend API calls\n"
        "- NODE_TLS_REJECT_UNAUTHORIZED: 0 for development (self-signed certs)\n\n"
        "Frontend uses .env.local (gitignored), backend uses .env with .env.example as template."
    )

    # --- SUMMARY TABLE ---
    pdf.add_page()
    pdf.section_title(6, "Technology Summary Table")

    headers = ["Technology", "Category", "Key Reason"]
    rows = [
        ["Next.js 13.4", "Framework", "SSR + App Router + file routing"],
        ["React 18", "UI Library", "Component model + Suspense + ecosystem"],
        ["TypeScript", "Language", "Type safety + IDE support + docs"],
        ["Tailwind CSS v3", "Styling", "Utility-first + purge + dark mode"],
        ["Framer Motion", "Animation", "Declarative + spring physics + layoutId"],
        ["Recharts", "Charting", "React-native D3 + composable + SVG"],
        ["TanStack Query v5", "Server State", "Caching + refetch + loading states"],
        ["Zustand", "Client State", "Minimal + no boilerplate + 1KB"],
        ["Axios", "HTTP Client", "Interceptors + auto-transform + timeout"],
        ["Lucide React", "Icons", "Tree-shakeable + consistent + 1000+ icons"],
        ["FastAPI", "Backend", "Async + auto-docs + Pydantic + Python ML"],
        ["HuggingFace API", "Inference", "Hosted inference + no GPU needed"],
        ["Uvicorn", "Server", "ASGI + hot-reload + high performance"],
        ["PostCSS", "CSS Pipeline", "Plugin system for Tailwind + prefixes"],
        ["Docker Compose", "DevOps", "One-command full-stack deployment"],
    ]

    pdf.set_font("Helvetica", "B", 9)
    pdf.set_fill_color(99, 102, 241)
    pdf.set_text_color(255, 255, 255)
    col_widths = [40, 30, 120]
    for i, h in enumerate(headers):
        pdf.cell(col_widths[i], 8, h, border=1, fill=True, align="C")
    pdf.ln()

    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(40, 40, 40)
    fill = False
    for row in rows:
        if fill:
            pdf.set_fill_color(240, 240, 255)
        else:
            pdf.set_fill_color(255, 255, 255)
        for i, cell in enumerate(row):
            pdf.cell(col_widths[i], 7, cell, border=1, fill=True)
        pdf.ln()
        fill = not fill

    path = os.path.join(OUTPUT_DIR, "1_Tech_Stack_and_Reasons.pdf")
    pdf.output(path)
    print(f"Generated: {path}")


# ============================================================
# PDF 2: TOPIC QUESTIONS (QLoRA / PEFT / Fine-Tuning)
# ============================================================
def generate_topic_questions_pdf():
    pdf = StyledPDF(
        "QLoRA & PEFT Interview Questions",
        "In-Depth Questions on Fine-Tuning, LoRA, Quantization & Training"
    )
    pdf.alias_nb_pages()
    pdf.add_cover()
    pdf.add_page()

    questions = [
        # PEFT Fundamentals
        (
            "What is PEFT (Parameter-Efficient Fine-Tuning) and why is it important?",
            "PEFT is a family of techniques that adapt large pre-trained language models to specific tasks "
            "by training only a small subset of parameters instead of the full model. Traditional full "
            "fine-tuning updates all billions of parameters, requiring enormous GPU memory (often 4-8x the "
            "model size for optimizer states and gradients). PEFT methods like LoRA, Prefix Tuning, P-Tuning, "
            "and Adapters achieve comparable performance by modifying less than 1% of parameters. "
            "This is important because: (1) It makes fine-tuning accessible on consumer GPUs (RTX 3090/4090 "
            "with 24GB VRAM can fine-tune a 7B model). (2) Storage is efficient -- you save only the small "
            "adapter weights (~10-50MB) instead of the full model (~14GB for 7B in fp16). (3) Multiple "
            "task-specific adapters can share one base model, enabling multi-tenant deployment. (4) It "
            "reduces catastrophic forgetting since most base model knowledge is preserved."
        ),
        (
            "Explain how LoRA (Low-Rank Adaptation) works mathematically.",
            "LoRA decomposes the weight update matrix into two low-rank matrices. For a pre-trained weight "
            "matrix W (d x k), instead of learning a full update Delta-W (d x k), LoRA learns two smaller "
            "matrices: A (d x r) and B (r x k), where r << min(d, k) is the rank. The forward pass becomes: "
            "h = Wx + (alpha/r) * BAx, where alpha is a scaling factor. During training, W is frozen and only "
            "A and B receive gradients. Matrix A is initialized with random Gaussian values and B with zeros, "
            "so the initial BA = 0 and training starts from the pre-trained weights. The rank r controls "
            "the expressiveness: r=8 for Llama 3 8B means each adapter layer has only 8 * (d_in + d_out) "
            "parameters instead of d_in * d_out. For a 4096x4096 attention matrix, this is 65,536 parameters "
            "instead of 16,777,216 -- a 256x reduction."
        ),
        (
            "What is QLoRA and how does it differ from standard LoRA?",
            "QLoRA (Quantized LoRA) combines 4-bit quantization of the base model with LoRA adapters trained "
            "in higher precision. The key innovations are: (1) 4-bit NormalFloat (NF4): A new data type "
            "optimally distributed for normally-distributed neural network weights, providing better precision "
            "than standard 4-bit integer quantization. (2) Double Quantization: The quantization constants "
            "themselves are quantized, saving an additional ~3GB for a 65B model. (3) Paged Optimizers: "
            "Uses NVIDIA unified memory to handle memory spikes during gradient checkpointing, preventing "
            "OOM errors. The base model is loaded in NF4 (~4GB for 7B params) while LoRA adapters and "
            "computations use bfloat16. Gradients flow through the quantized weights via a dequantization "
            "step during the forward pass. QLoRA achieves the same quality as full 16-bit fine-tuning "
            "while reducing memory from ~120GB to ~24GB for a 33B model."
        ),
        (
            "What is 4-bit NormalFloat (NF4) quantization and why is it better than INT4?",
            "NF4 is an information-theoretically optimal data type for normally distributed data. Neural "
            "network weights follow approximately normal distributions after pre-training. Standard INT4 "
            "divides the range uniformly into 16 bins, but this wastes precision on the tails where few "
            "weights exist. NF4 maps the 16 quantization bins to quantiles of the standard normal "
            "distribution, placing more bins where the density is highest (around zero). This means: "
            "(1) Values near zero (where most weights cluster) get finer granularity. (2) Outliers in the "
            "tails are still representable but with less precision. (3) The resulting quantization error "
            "is minimized for the actual weight distribution. Compared to INT4, NF4 preserves more "
            "information per bit, resulting in negligible quality loss even at 4 bits."
        ),
        (
            "What are the target modules in LoRA for Llama 3, and why these specific ones?",
            "For Llama 3 8B, the standard target modules are the attention projection matrices: "
            "q_proj (query), k_proj (key), v_proj (value), and o_proj (output). These are chosen because: "
            "(1) Attention layers are where the model learns relationships between tokens -- modifying them "
            "has the highest impact on task-specific behavior. (2) They are large matrices (4096x4096 for "
            "8B model) where low-rank approximation is most effective. (3) Research shows attention modules "
            "respond best to LoRA -- adapting just these 4 projections in each of 32 transformer layers "
            "is sufficient for most tasks. Some configurations also include gate_proj, up_proj, and "
            "down_proj (the MLP/FFN layers) for more expressive adaptation, but this increases trainable "
            "parameters. The q_proj + k_proj + v_proj + o_proj configuration hits the sweet spot of "
            "effectiveness vs efficiency."
        ),
        (
            "Explain the role of LoRA rank (r) and alpha (alpha). How do you choose them?",
            "Rank (r) determines the dimensionality of the low-rank decomposition. A higher rank means "
            "more parameters and more expressive power, but also more memory and computation. Common values "
            "are r=4, 8, 16, 32, 64. For most tasks, r=8 or r=16 is sufficient. Alpha controls the scaling "
            "of the LoRA update: the effective learning rate is scaled by alpha/r. A common heuristic is to "
            "set alpha = 2*r (e.g., alpha=16 for r=8). This means the LoRA update is scaled by a factor of 2. "
            "Higher alpha amplifies the adapter's influence -- useful when the task is very different from "
            "pre-training data. Lower alpha keeps the model closer to its pre-trained behavior. The ratio "
            "alpha/r is what matters: alpha=16, r=8 and alpha=32, r=16 have the same effective scaling. "
            "In this project, r=8 and alpha=32 (ratio=4) are used, which is a moderately strong adaptation."
        ),
        (
            "What is the trainable parameter percentage in QLoRA for Llama 3 8B, and how is it calculated?",
            "Llama 3 8B has approximately 8.03 billion total parameters. With QLoRA targeting q_proj, k_proj, "
            "v_proj, and o_proj with rank r=8: Each projection is 4096x4096. LoRA adds A (4096x8) and "
            "B (8x4096) = 65,536 params per projection. 4 projections per layer = 262,144 params per layer. "
            "32 transformer layers = 8,388,608 total trainable parameters. Trainable percentage = "
            "8,388,608 / 8,030,000,000 = 0.104%. In practice, with additional bias terms and normalization "
            "layers that may be unfrozen, this reaches approximately 0.085%. This means 99.9% of parameters "
            "remain frozen at their pre-trained values. The adapter weights are only ~33MB in bfloat16, "
            "compared to the full 14GB model."
        ),
        (
            "How does gradient checkpointing work and why is it used in QLoRA training?",
            "Gradient checkpointing (also called activation checkpointing) trades compute for memory during "
            "backpropagation. Normally, all intermediate activations from the forward pass are stored in memory "
            "for use during backpropagation. For a 32-layer model with large batch sizes, these activations "
            "can consume 20-40GB of GPU memory. With gradient checkpointing, only a subset of activations "
            "are retained (typically one per transformer layer). During backpropagation, the missing "
            "activations are recomputed on-the-fly from the nearest checkpoint. This reduces activation "
            "memory from O(n) to O(sqrt(n)) at the cost of roughly 33% more computation. In QLoRA, this "
            "is critical because the 4-bit base model already occupies most of the GPU memory, leaving "
            "minimal room for activations. Combined with paged optimizers that spill optimizer states "
            "to CPU RAM during memory spikes, gradient checkpointing makes 8B model training possible "
            "on a single 24GB GPU."
        ),
        (
            "What is the difference between full fine-tuning, LoRA, QLoRA, and Prefix Tuning?",
            "Full Fine-Tuning: Updates all model parameters. Requires 4-8x model size in GPU memory "
            "(weights + optimizer states + gradients). For Llama 3 8B in fp16: ~60GB+ VRAM. Highest "
            "quality but most expensive.\n\n"
            "LoRA: Freezes the base model (in fp16), trains low-rank adapter matrices. Memory: "
            "~32GB for 8B model (full fp16 weights + small adapter gradients). Adapters are small "
            "and portable. Quality very close to full fine-tuning.\n\n"
            "QLoRA: Same as LoRA but base model is 4-bit quantized (NF4). Memory: ~12-16GB for 8B "
            "model. Enables training on consumer GPUs. Same quality as LoRA through careful quantization.\n\n"
            "Prefix Tuning: Prepends learnable continuous vectors (soft prompts) to the input at each "
            "layer. Doesn't modify any weight matrices. Very few parameters (~0.01%) but less expressive. "
            "Best for simple classification tasks, struggles with complex generation.\n\n"
            "In practice, QLoRA is the best trade-off for most use cases: consumer GPU compatible, "
            "near-full-fine-tuning quality, small portable adapters."
        ),
        (
            "What training hyperparameters are important for QLoRA, and how do you tune them?",
            "Key hyperparameters:\n\n"
            "Learning Rate: Typically 1e-4 to 3e-4 for QLoRA (higher than full FT because fewer params "
            "are being updated). Use cosine schedule with warmup (5-10% of steps).\n\n"
            "Batch Size: Effective batch size = per_device_batch_size * gradient_accumulation_steps * "
            "num_gpus. Start with per_device=4, grad_accum=4 for effective batch of 16. Larger batches "
            "stabilize training but use more memory.\n\n"
            "Epochs: 1-3 epochs for large datasets, 3-5 for small datasets. QLoRA converges faster "
            "than full FT. Watch for overfitting with eval loss.\n\n"
            "LoRA Dropout: 0.05-0.1 recommended. Prevents overfitting the small adapter. Higher dropout "
            "(0.1) for small datasets.\n\n"
            "Max Sequence Length: 512-2048 tokens depending on task. Longer sequences use quadratically "
            "more memory due to attention.\n\n"
            "Weight Decay: 0.01-0.1. Regularization for the adapter weights.\n\n"
            "Warmup Steps: 5-10% of total steps. Prevents early training instability."
        ),
        (
            "How do you evaluate a fine-tuned model's quality? What metrics matter?",
            "Evaluation depends on the task type:\n\n"
            "For Generation Tasks: (1) Perplexity -- measures how well the model predicts the next token. "
            "Lower is better. Compare base vs fine-tuned on held-out domain data. (2) BLEU/ROUGE -- "
            "compare generated text to reference answers. ROUGE-L for summary-like tasks. (3) Human "
            "evaluation -- rate coherence, relevance, accuracy on a 1-5 scale.\n\n"
            "For Domain Adaptation: (1) Domain accuracy -- can the model correctly answer domain-specific "
            "questions? (2) Format compliance -- does it follow the desired output structure? "
            "(3) Hallucination rate -- does it fabricate facts? Compare against base model.\n\n"
            "Training Metrics to Monitor: (1) Training loss curve -- should decrease smoothly, plateau "
            "indicates convergence. (2) Eval loss -- divergence from training loss signals overfitting. "
            "(3) Learning rate schedule -- verify warmup and decay are smooth. (4) Gradient norms -- "
            "spikes indicate training instability, may need lower LR.\n\n"
            "This platform visualizes all these metrics on the Training Metrics page with interactive charts."
        ),
        (
            "What is catastrophic forgetting and how does QLoRA mitigate it?",
            "Catastrophic forgetting occurs when a model loses its general knowledge while learning new "
            "task-specific knowledge. In full fine-tuning, all parameters are updated, which can overwrite "
            "the representations learned during pre-training. QLoRA mitigates this in several ways:\n\n"
            "(1) Base model is frozen: 99.9% of parameters never change, preserving the vast majority "
            "of pre-trained knowledge.\n\n"
            "(2) Additive adaptation: LoRA adds to the existing weights (W + BA) rather than replacing "
            "them. The original behavior is always accessible as a baseline.\n\n"
            "(3) Low rank constraint: The rank-r decomposition limits how much the adapter can diverge "
            "from pre-trained behavior. Higher rank = more potential forgetting.\n\n"
            "(4) Training duration: Fewer epochs are needed compared to full FT, reducing exposure to "
            "forgetting.\n\n"
            "In practice, a QLoRA fine-tuned model retains >95% of its general capability while gaining "
            "domain expertise. You can verify this by testing on general benchmarks before and after."
        ),
        (
            "How do you merge LoRA adapters back into the base model for inference?",
            "After training, you have two options for inference:\n\n"
            "Option 1 - Separate Loading: Load the quantized base model and adapter separately. The PEFT "
            "library applies the adapter dynamically during the forward pass. This allows hot-swapping "
            "adapters (different tasks) without reloading the base model. Memory overhead is minimal.\n\n"
            "Option 2 - Merged Model: Use model.merge_and_unload() to permanently add the LoRA weights "
            "into the base model: W_merged = W + (alpha/r) * BA. This eliminates the adapter overhead "
            "during inference (no separate matrix multiplication), making inference slightly faster. "
            "The merged model can be quantized to any precision and deployed like a normal model.\n\n"
            "For deployment: Merge for single-task deployment (simpler, faster inference). Keep separate "
            "for multi-task deployment (one base model, multiple adapters). The HuggingFace Hub supports "
            "both: you can push the adapter-only repo (small upload) or the merged model."
        ),
        (
            "What is the role of the BitsAndBytes library in QLoRA?",
            "BitsAndBytes is the quantization backend that makes QLoRA possible. It provides:\n\n"
            "(1) 4-bit NF4 Quantization: Implements the NormalFloat4 data type with blockwise quantization "
            "(typically 64-element blocks). Each block has its own scaling factor.\n\n"
            "(2) Double Quantization: Quantizes the 32-bit scaling factors to 8-bit, saving ~0.37 bits "
            "per parameter (~3GB for a 65B model).\n\n"
            "(3) Dequantization Kernels: Custom CUDA kernels that efficiently convert NF4 back to "
            "bfloat16 during the forward pass for matrix multiplication.\n\n"
            "(4) Paged Optimizers: 8-bit Adam optimizer with automatic page management -- when GPU memory "
            "is full, optimizer states page to CPU RAM and back seamlessly.\n\n"
            "(5) BitsAndBytesConfig: Configuration class that specifies quantization settings: "
            "load_in_4bit=True, bnb_4bit_quant_type='nf4', bnb_4bit_compute_dtype=bfloat16, "
            "bnb_4bit_use_double_quant=True."
        ),
        (
            "How does the attention mechanism work in Llama 3, and how does LoRA modify it?",
            "Llama 3 uses Grouped-Query Attention (GQA) with Rotary Position Embeddings (RoPE):\n\n"
            "The input hidden state is projected into queries (Q), keys (K), and values (V) via linear "
            "layers. GQA uses 32 query heads but only 8 key-value heads (4:1 ratio), reducing memory "
            "during inference without quality loss. RoPE encodes position information directly into Q "
            "and K via rotation matrices, enabling better length generalization.\n\n"
            "Attention = softmax(QK^T / sqrt(d_k)) * V\n\n"
            "LoRA modifies this by adding low-rank updates to the projection matrices:\n"
            "Q = W_q * x + (alpha/r) * B_q * A_q * x\n"
            "K = W_k * x + (alpha/r) * B_k * A_k * x\n"
            "V = W_v * x + (alpha/r) * B_v * A_v * x\n"
            "O = W_o * attn + (alpha/r) * B_o * A_o * attn\n\n"
            "The frozen W matrices provide the pre-trained attention patterns, while the BA matrices "
            "learn task-specific adjustments. GQA's reduced KV heads mean fewer LoRA parameters for "
            "k_proj and v_proj compared to q_proj and o_proj."
        ),
        (
            "What datasets and data formats are suitable for QLoRA fine-tuning?",
            "QLoRA supports the same data formats as any fine-tuning approach:\n\n"
            "Instruction Format (most common): {instruction, input, output} triples formatted as chat "
            "templates. Example: '<|begin_of_text|><|start_header_id|>user<|end_header_id|>\\n"
            "{instruction}\\n{input}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\\n"
            "{output}<|eot_id|>'. This is Llama 3's native chat format.\n\n"
            "Completion Format: Raw text continuation where the model learns to continue documents. "
            "Good for domain knowledge injection (medical papers, legal documents).\n\n"
            "Conversation Format: Multi-turn dialogue with role markers. Ideal for chatbot training.\n\n"
            "Data Quality > Quantity: 1,000 high-quality domain-specific examples often outperform "
            "100,000 noisy ones. Clean, diverse, representative data is critical. Remove duplicates, "
            "fix formatting, verify factual accuracy. Dataset sizes: 500-10,000 examples is typical "
            "for domain adaptation; more for complex tasks."
        ),
        (
            "What are common failure modes during QLoRA training and how do you debug them?",
            "Common issues and solutions:\n\n"
            "1. Loss Not Decreasing: Learning rate too low, wrong data format (model can't parse the "
            "template), or data too noisy. Fix: increase LR to 2e-4, verify chat template formatting, "
            "inspect a few training examples manually.\n\n"
            "2. Loss Spikes: Learning rate too high or batch too small. Fix: reduce LR, increase "
            "gradient accumulation steps, add gradient clipping (max_grad_norm=1.0).\n\n"
            "3. Out of Memory (OOM): Sequence too long, batch too large, or gradient checkpointing "
            "not enabled. Fix: reduce max_seq_length, set per_device_batch=1 with more grad_accum, "
            "enable gradient_checkpointing=True.\n\n"
            "4. Eval Loss Diverging (Overfitting): Too many epochs, too little data, or rank too high. "
            "Fix: stop training earlier, add more data or augmentation, reduce LoRA rank, increase dropout.\n\n"
            "5. CUDA Errors: BitsAndBytes version mismatch with CUDA toolkit. Fix: match bitsandbytes "
            "version to installed CUDA version (e.g., bitsandbytes==0.41.1 for CUDA 11.8).\n\n"
            "6. Garbage Output: Wrong chat template or tokenizer mismatch. Verify tokenizer matches "
            "the base model and EOS tokens are correctly set."
        ),
        (
            "How do you deploy a QLoRA fine-tuned model to production?",
            "Deployment options from simplest to most scalable:\n\n"
            "1. HuggingFace Inference Endpoints: Push the merged model or adapter to HF Hub. Create an "
            "Inference Endpoint (managed GPU hosting). Scales automatically, supports auto-scaling. "
            "Cost: $1-5/hr depending on GPU.\n\n"
            "2. vLLM / TGI: Run vLLM or Text Generation Inference on your own GPU server. Supports "
            "continuous batching, paged attention, and LoRA adapter hot-swapping. Best throughput "
            "for high-volume APIs.\n\n"
            "3. GGUF + llama.cpp: Convert to GGUF format with quantization (Q4_K_M, Q5_K_M). Run on "
            "CPU or consumer GPU with llama.cpp. Good for edge deployment or low-cost hosting.\n\n"
            "4. AWS SageMaker / GCP Vertex AI: Managed ML endpoints with auto-scaling, A/B testing, "
            "and monitoring. Higher cost but enterprise-grade reliability.\n\n"
            "This platform uses option 1 (HF Inference API) with a 3-tier fallback for reliability."
        ),
        (
            "What is the impact of sequence length on QLoRA training memory and compute?",
            "Sequence length has a quadratic impact on memory due to the attention mechanism:\n\n"
            "Attention Memory = O(n^2 * d) where n is sequence length and d is head dimension.\n\n"
            "For Llama 3 8B with 32 attention heads: doubling sequence length from 512 to 1024 "
            "roughly quadruples the attention memory. Practical impacts:\n\n"
            "512 tokens: ~12GB VRAM, batch_size=4 possible on 24GB GPU\n"
            "1024 tokens: ~16GB VRAM, batch_size=2 on 24GB GPU\n"
            "2048 tokens: ~22GB VRAM, batch_size=1 on 24GB GPU\n"
            "4096 tokens: Requires 48GB+ GPU or gradient checkpointing + batch=1\n\n"
            "Llama 3 supports up to 8192 tokens natively (RoPE), but training at full context length "
            "is expensive. Best practice: set max_seq_length to the longest example in your dataset "
            "plus some margin, not the model's maximum. Most fine-tuning tasks work well with 512-1024."
        ),
        (
            "How does the platform's 3-tier fallback architecture ensure reliability?",
            "The backend implements a defensive architecture for the inference playground:\n\n"
            "Tier 1 - Live HuggingFace API: The service calls the HF Inference API with the configured "
            "model ID and API key. If the model is deployed and responsive, real inference results are "
            "returned with 'fallback: false'. Timeout: 30 seconds.\n\n"
            "Tier 2 - Response Cache: If the live API fails (model sleeping, rate limited, API key invalid), "
            "the system checks an in-memory cache of previous successful responses. Cache entries are "
            "matched by prompt similarity.\n\n"
            "Tier 3 - Keyword-Matched Mock Data: The fallback_data.py module contains MOCK_RESPONSE_PAIRS "
            "with 6 topic categories (geography, quantum physics, ML/DL comparison, biology, PEFT/fine-tuning, "
            "generic). The get_mock_response() function fuzzy-matches keywords from the user's prompt to "
            "select the most relevant mock. Each pair has distinct base vs fine-tuned responses.\n\n"
            "Every response includes metadata: fallback flag, response time, model ID used. The frontend "
            "shows a 'Demo Mode Active' banner when operating in fallback mode."
        ),
        (
            "Explain the concept of adapter merging and multi-adapter inference.",
            "Adapter merging combines multiple LoRA adapters trained for different tasks:\n\n"
            "Simple Merging: Average the adapter weights from multiple tasks. W_merged = W + "
            "mean(BA_task1, BA_task2, ...). Quick but may degrade per-task quality.\n\n"
            "TIES Merging: Trim small values, Elect signs by majority vote, Disjoint merge. Resolves "
            "conflicts between adapters more intelligently than averaging.\n\n"
            "DARE Merging: Randomly drops adapter parameters before merging, using dropout-like "
            "randomization to reduce interference between task-specific features.\n\n"
            "Multi-Adapter Inference: Load the base model once, maintain multiple adapters in memory. "
            "At inference time, select the appropriate adapter based on the request (e.g., medical "
            "adapter for health queries, legal adapter for law queries). Frameworks like vLLM support "
            "this natively with near-zero overhead for adapter switching.\n\n"
            "This is one of LoRA's greatest advantages: a single base model serves unlimited tasks "
            "with minimal storage (~30MB per adapter vs ~14GB per full model)."
        ),
    ]

    n = 1
    for i, (q, a) in enumerate(questions):
        if i == 5 or i == 10 or i == 15:
            pdf.add_page()
        pdf.question_block(n, q, a)
        n += 1

    path = os.path.join(OUTPUT_DIR, "2_QLoRA_PEFT_Topic_Questions.pdf")
    pdf.output(path)
    print(f"Generated: {path}")


# ============================================================
# PDF 3: MISCELLANEOUS QUESTIONS
# ============================================================
def generate_misc_questions_pdf():
    pdf = StyledPDF(
        "Miscellaneous Interview Questions",
        "System Design, Frontend, Backend, ML/AI, and Project Questions"
    )
    pdf.alias_nb_pages()
    pdf.add_cover()
    pdf.add_page()

    questions = [
        # --- SYSTEM DESIGN ---
        (
            "System Design",
            "How would you design a scalable inference platform for serving multiple fine-tuned models?",
            "Architecture overview: (1) API Gateway (Kong/AWS API Gateway) handles routing, auth, rate limiting. "
            "(2) Request Router examines the incoming request's model_id and routes to the correct model server. "
            "(3) Model Servers run vLLM or TGI instances, each hosting one base model with multiple LoRA adapters. "
            "Continuous batching groups concurrent requests for GPU efficiency. (4) Auto-Scaler (Kubernetes HPA or "
            "AWS SageMaker) monitors GPU utilization and request queue depth, scaling pods up/down. "
            "(5) Cache Layer (Redis) stores recent prompt-response pairs for identical requests. "
            "(6) Model Registry (MLflow or HF Hub) tracks model versions, adapters, and deployment metadata. "
            "(7) Monitoring (Prometheus + Grafana) tracks latency P50/P95/P99, throughput, GPU utilization, "
            "error rates. Key scaling decisions: batch size vs latency trade-off, when to split models across "
            "GPUs (tensor parallelism), adapter preloading strategy (LRU cache of hot adapters)."
        ),
        (
            "System Design",
            "How would you implement real-time streaming for token-by-token inference output?",
            "Use Server-Sent Events (SSE) for unidirectional streaming from server to client:\n\n"
            "Backend: FastAPI endpoint with StreamingResponse. The inference engine generates tokens one at a time "
            "using generate() with streamer=TextIteratorStreamer(). Each token is yielded as an SSE event: "
            "'data: {\"token\": \"word\", \"index\": 42}\\n\\n'. Include a [DONE] sentinel event.\n\n"
            "Frontend: Use the EventSource API or fetch() with ReadableStream. Parse each SSE event, append "
            "the token to the displayed text, and update the UI incrementally. TanStack Query's useQuery doesn't "
            "natively support streaming, so use a custom hook with useState + useEffect + EventSource.\n\n"
            "Why SSE over WebSocket: SSE is simpler (HTTP-based, auto-reconnect, no handshake protocol), "
            "unidirectional (server to client is all we need), and works through most proxies/CDNs. WebSocket "
            "is overkill for inference streaming where the client only sends one message (the prompt).\n\n"
            "This platform simulates this with a typing animation (setInterval revealing characters) since "
            "the HuggingFace Inference API doesn't support streaming in all configurations."
        ),
        (
            "System Design",
            "How do you handle rate limiting and abuse prevention for a public ML API?",
            "Multi-layer rate limiting strategy:\n\n"
            "Layer 1 - IP Rate Limiting (Nginx/CloudFlare): 60 requests/minute per IP. Blocks DDoS and "
            "basic abuse. Uses sliding window counter algorithm.\n\n"
            "Layer 2 - API Key Rate Limiting (Redis): Per-user quotas based on plan tier. Free: 100 req/day, "
            "Pro: 10,000 req/day, Enterprise: unlimited. Token bucket algorithm allows bursts while "
            "enforcing average rate.\n\n"
            "Layer 3 - Compute Budget: Track total GPU-seconds consumed per user. A 2048-token generation "
            "costs more than 128-token. Prevent users from consuming disproportionate compute.\n\n"
            "Layer 4 - Content Filtering: Check prompts against a blocklist and toxicity classifier before "
            "sending to GPU. Reject harmful prompts early to save compute.\n\n"
            "Implementation: Redis stores counters with TTL for sliding windows. Return 429 Too Many Requests "
            "with Retry-After header. Include X-RateLimit-Remaining headers so clients can self-throttle."
        ),
        (
            "Frontend Architecture",
            "Explain the difference between server components and client components in Next.js App Router.",
            "Server Components (default in App Router): Render on the server, send HTML to the client. "
            "Cannot use useState, useEffect, browser APIs, or event handlers. Benefits: zero JS sent to "
            "client, direct database/filesystem access, no hydration cost, better SEO. Use for: data fetching "
            "pages, static content, layout wrappers.\n\n"
            "Client Components (marked with 'use client'): Render on both server (SSR) and client (hydration). "
            "Can use all React hooks, event handlers, and browser APIs. Required for: interactivity (buttons, "
            "forms), animations (Framer Motion), third-party client libraries (Recharts, Zustand).\n\n"
            "In this project: Layout and page shells could be server components, but most components use "
            "client features (Framer Motion animations, theme context, TanStack Query). The 'use client' "
            "boundary is at the page level for interactive pages and at the component level for shared "
            "components. The key principle: push 'use client' as far down the tree as possible to keep "
            "the maximum amount of static HTML server-rendered."
        ),
        (
            "Frontend Architecture",
            "How does the CSS custom property theme system work, and why not use Tailwind's built-in dark mode?",
            "The theme system uses CSS custom properties (variables) defined in :root and .dark:\n\n"
            ":root { --bg-primary: #f8fafc; --text-primary: #0f172a; }\n"
            ".dark { --bg-primary: #0b1121; --text-primary: #f1f5f9; }\n\n"
            "Components reference these: style={{ background: 'var(--bg-primary)' }}. The ThemeProvider "
            "toggles the .dark class on <html>, and CSS instantly resolves all variables to their dark values.\n\n"
            "Why not Tailwind's dark: prefix? (1) Tailwind's 'dark:bg-slate-900' doubles the class count "
            "on every element, making JSX verbose and hard to read. (2) Custom properties work everywhere: "
            "inline styles, SVG fills, Recharts theme props, third-party components. Tailwind classes only "
            "work in Tailwind-aware contexts. (3) Glassmorphism tokens (--glass-bg with alpha channels) are "
            "much cleaner as variables than Tailwind arbitrary values. (4) A single global transition on "
            "background-color/color smoothly animates the theme switch -- impossible with Tailwind class swaps.\n\n"
            "The hybrid approach: Tailwind handles layout (grid, flex, padding, margin) while CSS variables "
            "handle colors and theming. Best of both worlds."
        ),
        (
            "Frontend Architecture",
            "How do skeleton loaders improve perceived performance compared to spinners?",
            "Skeleton loaders show a gray placeholder that matches the shape of the content being loaded. "
            "They improve UX in several ways:\n\n"
            "(1) Layout stability: Skeletons occupy the same space as the real content, preventing layout "
            "shift (CLS) when data arrives. Spinners centered on the page cause a jarring jump.\n\n"
            "(2) Perceived speed: Research shows users perceive skeleton-loaded pages as 10-20% faster than "
            "spinner-loaded pages at the same actual load time. The visual progression (skeleton -> content) "
            "feels like incremental loading rather than binary loading/loaded.\n\n"
            "(3) Context preservation: The skeleton's shape tells users what type of content is coming "
            "(chart, card, text), setting expectations. A generic spinner gives no information.\n\n"
            "(4) Shimmer animation: The gradient sweep animation (left to right) creates a sense of "
            "progress and activity. Static gray blocks feel broken; animated ones feel alive.\n\n"
            "Implementation in this project: SkeletonLoader.tsx provides variants (text, card, chart, circle). "
            "Each route has a loading.tsx file (Next.js convention) that renders route-specific skeletons. "
            "StatsCard renders a StatsCardSkeleton when its query is in loading state."
        ),
        (
            "Frontend Architecture",
            "How does Framer Motion's layoutId work for the nav indicator animation?",
            "layoutId enables shared layout animations between components that mount/unmount in different "
            "positions. In the Navbar, each nav link conditionally renders a motion.div with layoutId='nav-indicator' "
            "when that link is active. When the user navigates from /metrics to /playground:\n\n"
            "1. The indicator under 'Training' unmounts\n"
            "2. The indicator under 'Playground' mounts\n"
            "3. Because they share layoutId='nav-indicator', Framer Motion automatically animates the "
            "indicator sliding from one position to the other using FLIP (First, Last, Invert, Play).\n\n"
            "FLIP technique: (1) Record the element's FIRST position (under Training). (2) Calculate the "
            "LAST position (under Playground). (3) INVERT: apply a CSS transform to make it appear at the "
            "old position. (4) PLAY: animate the transform to zero, moving it to the new position.\n\n"
            "This creates a smooth sliding effect without managing absolute positioning or calculating "
            "pixel offsets manually. The animation uses spring physics (type: 'spring', stiffness: 350, "
            "damping: 30) for a natural, bouncy feel."
        ),
        (
            "Backend Architecture",
            "Why FastAPI over Flask/Django for an ML inference backend?",
            "FastAPI advantages for ML/AI projects:\n\n"
            "(1) Native Async: ML inference APIs often need to call external services (HuggingFace API, "
            "model servers). async/await enables non-blocking I/O -- one worker can handle multiple "
            "concurrent inference requests. Flask requires gunicorn workers (process-per-request).\n\n"
            "(2) Automatic API Documentation: OpenAPI/Swagger UI at /docs. Clients see exact request/response "
            "schemas. Critical for ML APIs where input/output shapes are complex.\n\n"
            "(3) Pydantic Validation: Request bodies are validated against Pydantic models automatically. "
            "Invalid temperature values (negative, >2.0) are rejected with clear error messages before "
            "reaching the inference code.\n\n"
            "(4) Python ML Ecosystem: Direct access to transformers, torch, bitsandbytes, datasets, "
            "huggingface_hub. No language boundary or subprocess management.\n\n"
            "(5) Performance: Built on Starlette and uvicorn, FastAPI benchmarks within 10% of Node.js "
            "and Go for I/O-bound workloads. The bottleneck is always the GPU inference, not the web framework.\n\n"
            "Django REST Framework is too heavy -- ORM, admin panel, migrations are unnecessary for a "
            "stateless inference API."
        ),
        (
            "Backend Architecture",
            "How does the compare_models endpoint achieve concurrent inference?",
            "The /api/inference/compare endpoint runs base and fine-tuned model inference simultaneously "
            "using asyncio.gather():\n\n"
            "async def compare_models(prompt, max_new_tokens, temperature):\n"
            "    base_task = call_inference_api(prompt, base_model_id, max_new_tokens, temperature)\n"
            "    ft_task = call_inference_api(prompt, finetuned_model_id, max_new_tokens, temperature)\n"
            "    base_result, ft_result = await asyncio.gather(base_task, ft_task, return_exceptions=True)\n\n"
            "Without gather, the calls would be sequential: base takes 2s + finetuned takes 1.5s = 3.5s total. "
            "With gather, both run concurrently: total time = max(2s, 1.5s) = 2s. This is a ~43% improvement.\n\n"
            "return_exceptions=True ensures that if one model fails, the other's result is still returned "
            "instead of both being lost. The frontend can show one real result and one error message.\n\n"
            "For mock responses, asyncio.sleep(random.uniform(0.8, 1.5)) simulates realistic latency. "
            "The gather ensures both simulated delays run concurrently too."
        ),
        (
            "Machine Learning",
            "What is the difference between pre-training, fine-tuning, and prompt engineering?",
            "Pre-training: Train a model from scratch on massive text corpora (trillions of tokens). "
            "The model learns language understanding, world knowledge, and reasoning. Requires thousands "
            "of GPUs over weeks/months. Cost: millions of dollars. Only done by large labs (Meta, Google, etc.).\n\n"
            "Fine-tuning: Take a pre-trained model and further train it on a smaller, task-specific dataset. "
            "The model adapts its existing knowledge to perform better on the target domain. With QLoRA, "
            "this can be done on a single consumer GPU in hours. Cost: $10-100 in cloud GPU time.\n\n"
            "Prompt Engineering: No training at all. Craft the input prompt to guide the pre-trained model's "
            "behavior. Techniques: few-shot examples, chain-of-thought reasoning, system prompts. Cost: $0 "
            "(just API calls). Limitations: context window limits, no permanent knowledge injection.\n\n"
            "When to use each: Prompt engineering first (cheapest, fastest iteration). If performance is "
            "insufficient, fine-tune with QLoRA. If the domain is extremely specialized (medical, legal, "
            "scientific), fine-tuning is almost always necessary. Pre-training is never done by end users."
        ),
        (
            "Machine Learning",
            "What are the key differences between Llama 3 and previous Llama models?",
            "Llama 3 improvements over Llama 2:\n\n"
            "(1) Tokenizer: New tiktoken-based tokenizer with 128K vocabulary (vs 32K in Llama 2). "
            "More efficient encoding, especially for non-English text and code. Reduces token count by "
            "~15% on average.\n\n"
            "(2) Attention: Grouped-Query Attention (GQA) for all sizes. Llama 2 only used GQA for "
            "70B; the 7B/13B used Multi-Head Attention. GQA reduces KV cache memory by 4x.\n\n"
            "(3) Training Data: 15T tokens (vs 2T for Llama 2). More diverse, higher quality, better "
            "filtering. Includes more code and multilingual data.\n\n"
            "(4) Context Length: 8192 tokens native (vs 4096 for Llama 2). Extended versions support "
            "up to 128K tokens with RoPE scaling.\n\n"
            "(5) Performance: Llama 3 8B matches or exceeds Llama 2 70B on many benchmarks. The "
            "instruction-tuned variant (Instruct) has much better instruction following.\n\n"
            "(6) License: More permissive community license allowing commercial use with attribution."
        ),
        (
            "Machine Learning",
            "What is Grouped-Query Attention (GQA) and how does it reduce inference cost?",
            "Standard Multi-Head Attention (MHA) uses separate Key and Value projections for each "
            "attention head. For Llama 3 8B with 32 heads and d_head=128: K and V each need "
            "32 * 128 = 4096 dimensions.\n\n"
            "GQA groups multiple query heads to share one set of K and V heads. Llama 3 uses 8 KV groups "
            "for 32 query heads (4:1 ratio). K and V only need 8 * 128 = 1024 dimensions.\n\n"
            "Impact on inference: The KV cache stores all previous tokens' K and V for autoregressive "
            "generation. With MHA: KV cache = 2 * 32 * 128 * seq_len * num_layers bytes. With GQA (8 groups): "
            "KV cache = 2 * 8 * 128 * seq_len * num_layers bytes -- 4x reduction.\n\n"
            "For Llama 3 8B generating 2048 tokens: MHA KV cache would be ~8GB, GQA KV cache is ~2GB. "
            "This directly translates to higher batch sizes (more concurrent users) on the same GPU.\n\n"
            "Training: GQA is learned during pre-training. Quality is within 1% of MHA on most benchmarks, "
            "making it a free lunch for inference efficiency."
        ),
        (
            "DevOps & Deployment",
            "How would you set up CI/CD for a project like this PEFT platform?",
            "CI/CD pipeline using GitHub Actions:\n\n"
            "PR Checks (on every push): (1) Frontend: npm install -> TypeScript typecheck (tsc --noEmit) -> "
            "ESLint -> unit tests (Jest/Vitest) -> build (next build). (2) Backend: pip install -> pytest -> "
            "mypy type checking -> ruff linting. (3) Docker: Build images to verify Dockerfiles work.\n\n"
            "Staging Deploy (on merge to main): (1) Build Docker images, tag with commit SHA. (2) Push to "
            "container registry (ECR/GHCR). (3) Deploy to staging environment. (4) Run integration tests "
            "against staging (API health checks, Playwright E2E tests).\n\n"
            "Production Deploy (manual trigger or tag): (1) Deploy to production with rolling update. "
            "(2) Health check verification. (3) Automatic rollback if health checks fail.\n\n"
            "ML-Specific: (4) Model deployment pipeline: when a new adapter is pushed to HuggingFace Hub, "
            "trigger a model quality check (eval on test set), then update the HF_FINETUNED_MODEL_ID "
            "environment variable in production."
        ),
        (
            "DevOps & Deployment",
            "How do you handle environment variables and secrets in a full-stack ML application?",
            "Layered secrets management:\n\n"
            "Development: .env.local (gitignored) for frontend, .env (gitignored) for backend. "
            ".env.example files with placeholder values are committed as documentation.\n\n"
            "CI/CD: GitHub Actions secrets (Settings -> Secrets). Referenced as ${{ secrets.HF_API_KEY }} "
            "in workflow YAML. Never printed to logs (masked automatically).\n\n"
            "Production: (1) AWS Secrets Manager or HashiCorp Vault for HF API keys. (2) Kubernetes Secrets "
            "mounted as environment variables in pods. (3) Rotate keys regularly with zero-downtime rotation.\n\n"
            "Key variables in this project: HUGGINGFACE_API_KEY (sensitive -- never commit), HF_BASE_MODEL_ID "
            "(meta-llama/Meta-Llama-3-8B-Instruct), HF_FINETUNED_MODEL_ID (user-specific), "
            "NEXT_PUBLIC_API_URL (public -- prefixed with NEXT_PUBLIC_ for client-side access).\n\n"
            "Critical rule: NEXT_PUBLIC_ prefix variables are embedded in the JavaScript bundle and visible "
            "to all users. Never put API keys in NEXT_PUBLIC_ variables."
        ),
        (
            "Project & Process",
            "What was the most challenging part of building this PEFT platform?",
            "Several interconnected challenges:\n\n"
            "(1) Tailwind v4 vs v3 Compatibility: The project initially used Tailwind v4 with its new "
            "CSS-first configuration (@import 'tailwindcss'). This is incompatible with Next.js 13's "
            "webpack-based PostCSS pipeline. The CSS custom properties loaded fine but zero utility classes "
            "were generated, resulting in a completely broken layout. The fix required downgrading to "
            "Tailwind v3 with traditional @tailwind directives and postcss.config.js.\n\n"
            "(2) 3-Tier Fallback System: Designing the backend to work without a deployed HuggingFace model "
            "required careful keyword matching for mock responses, distinct base vs fine-tuned response "
            "pairs, and simulated latency. Every API response needed metadata flags so the frontend could "
            "accurately display connection status.\n\n"
            "(3) Theme System Architecture: Choosing between Tailwind's dark: prefix, CSS custom properties, "
            "CSS-in-JS, or a combination. The hybrid approach (Tailwind for layout, CSS vars for colors) "
            "required ensuring every component -- including third-party Recharts tooltips and SVG "
            "diagrams -- respected the theme variables.\n\n"
            "(4) Animation Performance: Framer Motion animations needed to be scroll-triggered (whileInView) "
            "to avoid janking the initial page load. The typing animation required careful state management "
            "to avoid stale closures in setInterval callbacks."
        ),
        (
            "Project & Process",
            "How does this project demonstrate production-readiness despite being a portfolio project?",
            "Production-grade practices implemented:\n\n"
            "(1) Error Boundaries: Every route has an error.tsx that catches rendering errors and shows "
            "a themed retry UI instead of a white screen.\n\n"
            "(2) Loading States: Every route has a loading.tsx with content-specific skeletons. No blank "
            "white pages during data fetching.\n\n"
            "(3) Fallback Architecture: The 3-tier system ensures the app works with or without external "
            "services. Graceful degradation, not hard failure.\n\n"
            "(4) Responsive Design: Full mobile support with hamburger menu, responsive grids, "
            "and appropriate typography scaling.\n\n"
            "(5) Accessibility: Semantic HTML, ARIA labels on interactive elements, keyboard navigation "
            "support (Ctrl+Enter in playground), sufficient color contrast.\n\n"
            "(6) Performance: Tree-shaking (Lucide icons), code splitting (Next.js automatic), "
            "font optimization (next/font), skeleton loaders (perceived performance).\n\n"
            "(7) Type Safety: Full TypeScript coverage, Pydantic validation on backend.\n\n"
            "(8) Clean Architecture: Layered components, separated state management, clear API contracts."
        ),
        (
            "General Technical",
            "What is glassmorphism and when is it appropriate to use?",
            "Glassmorphism is a UI design trend characterized by:\n"
            "- Semi-transparent backgrounds (rgba with alpha 0.5-0.8)\n"
            "- Background blur (backdrop-filter: blur(10-20px))\n"
            "- Subtle borders (often white with low opacity)\n"
            "- Layered depth with soft shadows\n\n"
            "When to use: (1) Dashboard/data-heavy UIs where visual hierarchy is important. (2) Dark mode "
            "UIs where the frosted effect adds depth. (3) Cards overlaying gradient or image backgrounds. "
            "(4) Premium/modern-feeling applications.\n\n"
            "When NOT to use: (1) Text-heavy content (readability suffers behind blur). (2) Accessibility-"
            "critical applications (low contrast can fail WCAG). (3) Low-powered devices (backdrop-filter "
            "is GPU-intensive). (4) Browsers without backdrop-filter support (provide a solid fallback).\n\n"
            "In this project, glassmorphism is used for cards, the navbar, and tooltip overlays -- elements "
            "where the frosted effect adds depth without compromising readability. Text always uses fully "
            "opaque colors against the glass background."
        ),
        (
            "General Technical",
            "Explain the concept of tree-shaking and how it applies to this project.",
            "Tree-shaking is a dead-code elimination technique used by bundlers (webpack, Rollup, esbuild) "
            "to remove unused exports from the final JavaScript bundle.\n\n"
            "How it works: The bundler analyzes ES module import/export statements to build a dependency "
            "graph. Any export that is never imported anywhere in the graph is removed. This only works "
            "with static ES module syntax (import/export), not CommonJS (require).\n\n"
            "In this project:\n"
            "- Lucide React: 'import { Sun, Moon } from \"lucide-react\"' only bundles those 2 icons, "
            "not all 1000+. Each icon is a separate module entry.\n"
            "- Framer Motion: 'import { motion, AnimatePresence } from \"framer-motion\"' only pulls "
            "the animation core, not the gesture system or SVG utilities.\n"
            "- Recharts: 'import { AreaChart, XAxis, Tooltip } from \"recharts\"' avoids bundling "
            "unused chart types like Sankey or Treemap.\n\n"
            "Next.js performs tree-shaking automatically during 'next build'. The development server "
            "bundles more liberally for faster rebuilds, so production bundles are always smaller."
        ),
        (
            "General Technical",
            "What is the difference between SSR, SSG, and ISR in Next.js?",
            "Server-Side Rendering (SSR): Pages are rendered on the server for every request. The server "
            "fetches data, generates HTML, and sends the complete page. Pros: always fresh data, good SEO. "
            "Cons: higher TTFB (time to first byte), server load per request.\n\n"
            "Static Site Generation (SSG): Pages are pre-rendered at build time. The HTML is generated once "
            "and served from CDN for all requests. Pros: fastest TTFB, minimal server cost. Cons: data can "
            "be stale until next build, long build times for many pages.\n\n"
            "Incremental Static Regeneration (ISR): SSG with a revalidation interval. After the interval "
            "expires, the next request triggers a background regeneration. The stale page is served while "
            "the new one builds. Pros: SSG speed + data freshness. Cons: slight staleness window.\n\n"
            "In this project: Pages are client-side rendered (CSR) with TanStack Query fetching data "
            "after mount. This is because the data comes from the FastAPI backend which may return "
            "different results (live vs fallback) depending on external service status. The loading.tsx "
            "skeletons provide a good UX during the client-side data fetch."
        ),
    ]

    n = 1
    current_category = ""
    for i, (category, q, a) in enumerate(questions):
        if category != current_category:
            pdf.add_page()
            pdf.section_title("", category)
            current_category = category
        pdf.question_block(n, q, a)
        n += 1

    path = os.path.join(OUTPUT_DIR, "3_Miscellaneous_Questions.pdf")
    pdf.output(path)
    print(f"Generated: {path}")


if __name__ == "__main__":
    generate_tech_stack_pdf()
    generate_topic_questions_pdf()
    generate_misc_questions_pdf()
    print("\nAll 3 PDFs generated successfully!")
