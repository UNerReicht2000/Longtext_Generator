# Longtext Generator for KRL

- [Longtext Generator for KRL](#longtext-generator-for-krl)
  - [1. Longtext Generator](#1-longtext-generator)
    - [Motivation](#motivation)
    - [Main Features](#main-features)
    - [Target Audience](#target-audience)
  - [2. License Notice for Companies](#2-license-notice-for-companies)
  - [3. Documentation](#3-documentation)
    - [1. Setup](#1-setup)
    - [2. User Interface](#2-user-interface)
    - [3. Longtext Tools](#3-longtext-tools)
      - [1. Clean Longtext](#1-clean-longtext)
        - [Sample (.csv)](#sample-csv)
      - [2. Delete Empty Lines](#2-delete-empty-lines)
      - [3. Merge Longtext](#3-merge-longtext)

## 1. Longtext Generator

**Longtext Generator** is an open-source tool for automated creation and editing of longtexts, designed for KUKA **KRL** code.

### Motivation

To simplify and automate the creation and maintenance of longtexts used with KUKA robots.

### Main Features

- Automated generation of longtexts from KUKA KRL source code.
- Flexible editing and customization of texts.
- Import support for common text file formats (.dat, .txt, .csv, ...).
- User-friendly interface.
- Longtext tools for common preprocessing tasks.

### Target Audience

This project is intended for engineers, technicians, and developers working with KUKA robots.

## 2. License Notice for Companies

This project is licensed under the **GNU GPL v3**.  
This means:

**Internal Use:**  
Companies are free to use the tool internally, including in commercial projects, as long as it is used internally.  
There is **no obligation** to disclose the source code if the software is not redistributed.

**Distribution:**  
If the tool or a modified version is distributed to third parties (e.g., customers), the **source code must be provided** and any modifications must also be released under **GPL v3**.

**Modifications:**  
Companies may modify the tool. Modifications must only be shared publicly if the modified version is **distributed**.

**Disclaimer:**  
The tool is provided **“as is”** without any warranty. Use it at your own risk.

In short: **Internal use is always allowed.** Obligations to release the code only apply when the software is distributed externally.

## 3. Documentation

### 1. Setup

[Setup instructions go here.]

### 2. User Interface

[User interface information goes here.]

### 3. Longtext Tools

#### 1. Clean Longtext

Using **Clean Longtext**, unnecessary characters are removed from the longtext to avoid formatting errors on the robot SmartPad.

##### Sample (.csv)

- before
    ```csv
    $IN[1]; Input1;
    $IN[2]; Input2;;
    $IN[3];
    ```
- after
    ```csv
    $IN[1]; Input1
    $IN[2]; Input2
    $IN[3]
    ```

#### 2. Delete Empty Lines

The **Delete Empty Lines** tool removes all lines that are empty.

> [!TIP]
> This function can be used to create an updated version of the longtext.

#### 3. Merge Longtext

Combine multiple longtext files into a single longtext file.
