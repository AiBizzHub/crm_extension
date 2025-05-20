# CRM Extension for ERPNext

**CRM Extension** is a custom Frappe application that integrates external CRM systems with ERPNext. It centralizes customer data, streamlines workflows, and ensures data consistency across platforms.

---

## ✨ Features

- **Seamless CRM Integration**: Connects ERPNext with third-party CRM systems effortlessly.
- **Real-Time Data Sync**: Keeps data consistent between ERPNext and external CRMs.
- **Lightweight & Modular**: Designed for efficiency and easy customization.
- **Configurable**: Simple setup with flexible extension options.

---

## 📦 Installation

Follow these steps to install the CRM Extension on your ERPNext (v15) instance:

### 1. Clone the Repository

```bash
cd ~/frappe-bench/apps
git clone https://github.com/intencodeindia/crm_extension.git
```

### 2. Install the App

```bash
bench --site your-site-name install-app crm_extension
```

Replace `your-site-name` with the name of your ERPNext site.

### 3. Restart Bench

```bash
bench restart
```

---

## 📂 Project Structure

```
crm_extension/
├── crm_extension/        # Core application module
├── .github/              # GitHub workflows and configurations
├── .gitignore            # Git ignore rules
├── license.txt           # License file
├── pyproject.toml        # Python project configuration
└── README.md             # This file
```

---

## 📋 Requirements

- **ERPNext**: v15.x
- **Frappe Framework**: v15.x
- **Python**: 3.10 or higher

---

## 📜 License

This project is licensed under the MIT License. See the `license.txt` file for details.

---

## 👨‍💻 Maintainers

Developed and maintained by [Intencode India](https://github.com/intencodeindia).

---

## 🤝 Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m 'Add your feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Open a Pull Request.

For major changes, please open an issue first to discuss your ideas.

---

## 📬 Support

For questions or support, open an issue on [GitHub](https://github.com/intencodeindia/crm_extension/issues) or contact the maintainers.
