---
title: "LanguageCode"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-core-language-code"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>LanguageCode</title>
    <link href="../../../images/logo-icon.svg" rel="icon" type="image/svg">
    <script>var pathToRoot = "../../../";</script>
    <script>document.documentElement.classList.replace("no-js","js");</script>
    <script>const storage = localStorage.getItem("dokka-dark-mode")
    if (storage == null) {
        const osDarkSchemePreferred = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches
        if (osDarkSchemePreferred === true) {
            document.getElementsByTagName("html")[0].classList.add("theme-dark")
        }
    } else {
        const savedDarkMode = JSON.parse(storage)
        if(savedDarkMode === true) {
            document.getElementsByTagName("html")[0].classList.add("theme-dark")
        }
    }
    </script>
<script type="text/javascript" src="https://unpkg.com/kotlin-playground@1/dist/playground.min.js" async="async"></script>
<script type="text/javascript" src="../../../scripts/sourceset_dependencies.js" async="async"></script>
<link href="../../../styles/style.css" rel="Stylesheet">
<link href="../../../styles/main.css" rel="Stylesheet">
<link href="../../../styles/prism.css" rel="Stylesheet">
<link href="../../../styles/logo-styles.css" rel="Stylesheet">
<link href="../../../styles/font-jb-sans-auto.css" rel="Stylesheet">
<link href="../../../ui-kit/ui-kit.min.css" rel="Stylesheet">
<script type="text/javascript" src="../../../scripts/clipboard.js" async="async"></script>
<script type="text/javascript" src="../../../scripts/navigation-loader.js" async="async"></script>
<script type="text/javascript" src="../../../scripts/platform-content-handler.js" async="async"></script>
<script type="text/javascript" src="../../../scripts/main.js" defer="defer"></script>
<script type="text/javascript" src="../../../scripts/prism.js" async="async"></script>
<script type="text/javascript" src="../../../ui-kit/ui-kit.min.js" defer="defer"></script>
<script type="text/javascript" src="../../../scripts/symbol-parameters-wrapper_deferred.js" defer="defer"></script>
</head>
<body>
    <div class="root">
    <nav class="navigation theme-dark" id="navigation-wrapper">
            <a class="library-name--link" href="../../../index.html">
                    API Reference
            </a>
        <button class="navigation-controls--btn navigation-controls--btn_toc ui-kit_mobile-only" id="toc-toggle"
                type="button">Toggle table of contents
        </button>
        <div class="navigation-controls--break ui-kit_mobile-only"></div>
        <div class="library-version" id="library-version">
        </div>
        <div class="navigation-controls">
        <div class="filter-section filter-section_loading" id="filter-section">
                <button class="platform-tag platform-selector jvm-like" data-active=""
                        data-filter=":modules:dokkaHtml/release">androidJvm</button>
            <div class="dropdown filter-section--dropdown" data-role="dropdown" id="filter-section-dropdown">
                <button class="button button_dropdown filter-section--dropdown-toggle" role="combobox"
                        data-role="dropdown-toggle"
                        aria-controls="platform-tags-listbox"
                        aria-haspopup="listbox"
                        aria-expanded="false"
                        aria-label="Toggle source sets"
                ></button>
                <ul role="listbox" id="platform-tags-listbox" class="dropdown--list" data-role="dropdown-listbox">
                    <div class="dropdown--header"><span>Platform filter</span>
                        <button class="button" data-role="dropdown-toggle" aria-label="Close platform filter">
                            <i class="ui-kit-icon ui-kit-icon_cross"></i>
                        </button>
                    </div>
                        <li role="option" class="dropdown--option platform-selector-option jvm-like" tabindex="0">
                            <label class="checkbox">
                                <input type="checkbox" class="checkbox--input" id=":modules:dokkaHtml/release"
                                       data-filter=":modules:dokkaHtml/release"/>
                                <span class="checkbox--icon"></span>
                                androidJvm
                            </label>
                        </li>
                </ul>
                <div class="dropdown--overlay"></div>
            </div>
        </div>
            <button class="navigation-controls--btn navigation-controls--btn_theme" id="theme-toggle-button"
                    type="button">Switch theme
            </button>
            <div class="navigation-controls--btn navigation-controls--btn_search" id="searchBar" role="button">Search in
                API
            </div>
        </div>
    </nav>
        <div id="container">
            <div class="sidebar" id="leftColumn">
                <div class="dropdown theme-dark_mobile" data-role="dropdown" id="toc-dropdown">
                    <ul role="listbox" id="toc-listbox" class="dropdown--list dropdown--list_toc-list"
                        data-role="dropdown-listbox">
                        <div class="dropdown--header">
                            <span>
                                    API Reference
                            </span>
                            <button class="button" data-role="dropdown-toggle" aria-label="Close table of contents">
                                <i class="ui-kit-icon ui-kit-icon_cross"></i>
                            </button>
                        </div>
                        <div class="sidebar--inner" id="sideMenu"></div>
                    </ul>
                    <div class="dropdown--overlay"></div>
                </div>
            </div>
            <div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.core/LanguageCode///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.core</a><span class="delimiter">/</span><span class="current">LanguageCode</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Language</span><wbr></wbr><span><span>Code</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="index.html">LanguageCode</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="index.html">LanguageCode</a><span class="token operator">&gt; </span></div><p class="paragraph">This enum represents language codes. The basic naming pattern consists of a 2-letter ISO 639-1 language code followed by a 2-letter ISO 3166-1 country code. Some language codes consist only of a language code, i.e. without a country code. When there is no ISO 639-1 language code, the related ISO 639-2 or ISO 639-3 language code is used. In case the script is specified, its ISO 15924 code is used.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button><button class="section-tab" data-togglable="ENTRY">Entries</button></div>
    <div class="tabs-section-body">
      <div data-togglable="ENTRY">
        <h2 class="">Entries</h2>
        <div class="table"><a data-name="-841883158%2FClasslikes%2F1617540583" anchor-label="EN_US" id="-841883158%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-e-n_-u-s/index.html">EN_US</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-841883158%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-e-n_-u-s/index.html">EN_US</a></div></div><div class="brief "><p class="paragraph">English (United States)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-4157257%2FClasslikes%2F1617540583" anchor-label="AF_ZA" id="-4157257%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-a-f_-z-a/index.html">AF_ZA</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-4157257%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-a-f_-z-a/index.html">AF_ZA</a></div></div><div class="brief "><p class="paragraph">Afrikaans</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-569732190%2FClasslikes%2F1617540583" anchor-label="SQ_AL" id="-569732190%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-q_-a-l/index.html">SQ_AL</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-569732190%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-s-q_-a-l/index.html">SQ_AL</a></div></div><div class="brief "><p class="paragraph">Albanian</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="76235032%2FClasslikes%2F1617540583" anchor-label="AM_ET" id="76235032%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-a-m_-e-t/index.html">AM_ET</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="76235032%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-a-m_-e-t/index.html">AM_ET</a></div></div><div class="brief "><p class="paragraph">Amharic (Ethiopia)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1798536978%2FClasslikes%2F1617540583" anchor-label="AR_SA" id="1798536978%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-a-r_-s-a/index.html">AR_SA</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1798536978%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-a-r_-s-a/index.html">AR_SA</a></div></div><div class="brief "><p class="paragraph">Arabic (Saudi Arabia)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1531996272%2FClasslikes%2F1617540583" anchor-label="HY_AM" id="-1531996272%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-h-y_-a-m/index.html">HY_AM</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1531996272%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-h-y_-a-m/index.html">HY_AM</a></div></div><div class="brief "><p class="paragraph">Armenian</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2059278392%2FClasslikes%2F1617540583" anchor-label="AS_IN" id="-2059278392%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-a-s_-i-n/index.html">AS_IN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2059278392%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-a-s_-i-n/index.html">AS_IN</a></div></div><div class="brief "><p class="paragraph">Assamese (India)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="568151029%2FClasslikes%2F1617540583" anchor-label="AZ_LATN_AZ" id="568151029%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-a-z_-l-a-t-n_-a-z/index.html">AZ_LATN_AZ</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="568151029%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-a-z_-l-a-t-n_-a-z/index.html">AZ_LATN_AZ</a></div></div><div class="brief "><p class="paragraph">Azeri - Latin</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1947869877%2FClasslikes%2F1617540583" anchor-label="BN_BD" id="-1947869877%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-b-n_-b-d/index.html">BN_BD</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1947869877%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-b-n_-b-d/index.html">BN_BD</a></div></div><div class="brief "><p class="paragraph">Bangla (Bangladesh)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1872131346%2FClasslikes%2F1617540583" anchor-label="BN_IN" id="-1872131346%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-b-n_-i-n/index.html">BN_IN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1872131346%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-b-n_-i-n/index.html">BN_IN</a></div></div><div class="brief "><p class="paragraph">Bangla (India)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-243100461%2FClasslikes%2F1617540583" anchor-label="EU_ES" id="-243100461%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-e-u_-e-s/index.html">EU_ES</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-243100461%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-e-u_-e-s/index.html">EU_ES</a></div></div><div class="brief "><p class="paragraph">Basque</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-958464631%2FClasslikes%2F1617540583" anchor-label="BE_BY" id="-958464631%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-b-e_-b-y/index.html">BE_BY</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-958464631%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-b-e_-b-y/index.html">BE_BY</a></div></div><div class="brief "><p class="paragraph">Belarusian</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1127791725%2FClasslikes%2F1617540583" anchor-label="BS_LATN_BA" id="-1127791725%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-b-s_-l-a-t-n_-b-a/index.html">BS_LATN_BA</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1127791725%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-b-s_-l-a-t-n_-b-a/index.html">BS_LATN_BA</a></div></div><div class="brief "><p class="paragraph">Bosnian - Latin</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-667721419%2FClasslikes%2F1617540583" anchor-label="BG_BG" id="-667721419%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-b-g_-b-g/index.html">BG_BG</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-667721419%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-b-g_-b-g/index.html">BG_BG</a></div></div><div class="brief "><p class="paragraph">Bulgarian</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2140105445%2FClasslikes%2F1617540583" anchor-label="CA_ES" id="2140105445%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-c-a_-e-s/index.html">CA_ES</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2140105445%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-c-a_-e-s/index.html">CA_ES</a></div></div><div class="brief "><p class="paragraph">Catalan (Spain)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="647219709%2FClasslikes%2F1617540583" anchor-label="KU_ARAB" id="647219709%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-k-u_-a-r-a-b/index.html">KU_ARAB</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="647219709%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-k-u_-a-r-a-b/index.html">KU_ARAB</a></div></div><div class="brief "><p class="paragraph">Central Kurdish - Arabic</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-91833070%2FClasslikes%2F1617540583" anchor-label="ZH_CN" id="-91833070%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-z-h_-c-n/index.html">ZH_CN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-91833070%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-z-h_-c-n/index.html">ZH_CN</a></div></div><div class="brief "><p class="paragraph">Chinese (Simplified China)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1245479850%2FClasslikes%2F1617540583" anchor-label="ZH_HK" id="1245479850%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-z-h_-h-k/index.html">ZH_HK</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1245479850%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-z-h_-h-k/index.html">ZH_HK</a></div></div><div class="brief "><p class="paragraph">Chinese (Traditional Hong Kong)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-575216342%2FClasslikes%2F1617540583" anchor-label="ZH_TW" id="-575216342%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-z-h_-t-w/index.html">ZH_TW</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-575216342%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-z-h_-t-w/index.html">ZH_TW</a></div></div><div class="brief "><p class="paragraph">Chinese (Traditional Taiwan)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1561913109%2FClasslikes%2F1617540583" anchor-label="HR_HR" id="1561913109%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-h-r_-h-r/index.html">HR_HR</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1561913109%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-h-r_-h-r/index.html">HR_HR</a></div></div><div class="brief "><p class="paragraph">Croatian</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="838097692%2FClasslikes%2F1617540583" anchor-label="CS_CZ" id="838097692%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-c-s_-c-z/index.html">CS_CZ</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="838097692%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-c-s_-c-z/index.html">CS_CZ</a></div></div><div class="brief "><p class="paragraph">Czech</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-396889921%2FClasslikes%2F1617540583" anchor-label="DA_DK" id="-396889921%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-d-a_-d-k/index.html">DA_DK</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-396889921%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-d-a_-d-k/index.html">DA_DK</a></div></div><div class="brief "><p class="paragraph">Danish</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2066537018%2FClasslikes%2F1617540583" anchor-label="PRS_ARAB_AF" id="2066537018%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-p-r-s_-a-r-a-b_-a-f/index.html">PRS_ARAB_AF</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2066537018%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-p-r-s_-a-r-a-b_-a-f/index.html">PRS_ARAB_AF</a></div></div><div class="brief "><p class="paragraph">Dari - Arabic (Afghanistan)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="332932698%2FClasslikes%2F1617540583" anchor-label="NL_BE" id="332932698%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-n-l_-b-e/index.html">NL_BE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="332932698%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-n-l_-b-e/index.html">NL_BE</a></div></div><div class="brief "><p class="paragraph">Flemish Dutch (Belgium)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1745984149%2FClasslikes%2F1617540583" anchor-label="NL_NL" id="1745984149%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-n-l_-n-l/index.html">NL_NL</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1745984149%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-n-l_-n-l/index.html">NL_NL</a></div></div><div class="brief "><p class="paragraph">Dutch</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="502365031%2FClasslikes%2F1617540583" anchor-label="EN_GB" id="502365031%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-e-n_-g-b/index.html">EN_GB</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="502365031%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-e-n_-g-b/index.html">EN_GB</a></div></div><div class="brief "><p class="paragraph">English (British)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="313375014%2FClasslikes%2F1617540583" anchor-label="ET_EE" id="313375014%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-e-t_-e-e/index.html">ET_EE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="313375014%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-e-t_-e-e/index.html">ET_EE</a></div></div><div class="brief "><p class="paragraph">Estonian</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1776977565%2FClasslikes%2F1617540583" anchor-label="FA_IR" id="-1776977565%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-f-a_-i-r/index.html">FA_IR</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1776977565%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-f-a_-i-r/index.html">FA_IR</a></div></div><div class="brief "><p class="paragraph">Farsi (Iran)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1755437568%2FClasslikes%2F1617540583" anchor-label="FIL_PH" id="-1755437568%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-f-i-l_-p-h/index.html">FIL_PH</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1755437568%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-f-i-l_-p-h/index.html">FIL_PH</a></div></div><div class="brief "><p class="paragraph">Filipino</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1608611957%2FClasslikes%2F1617540583" anchor-label="FI_FI" id="1608611957%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-f-i_-f-i/index.html">FI_FI</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1608611957%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-f-i_-f-i/index.html">FI_FI</a></div></div><div class="brief "><p class="paragraph">Finnish</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1603409963%2FClasslikes%2F1617540583" anchor-label="FR_FR" id="-1603409963%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-f-r_-f-r/index.html">FR_FR</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1603409963%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-f-r_-f-r/index.html">FR_FR</a></div></div><div class="brief "><p class="paragraph">French</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="819561447%2FClasslikes%2F1617540583" anchor-label="FR_CA" id="819561447%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-f-r_-c-a/index.html">FR_CA</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="819561447%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-f-r_-c-a/index.html">FR_CA</a></div></div><div class="brief "><p class="paragraph">French (Canada)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1678709954%2FClasslikes%2F1617540583" anchor-label="GL_ES" id="-1678709954%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-g-l_-e-s/index.html">GL_ES</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1678709954%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-g-l_-e-s/index.html">GL_ES</a></div></div><div class="brief "><p class="paragraph">Galician</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1877584611%2FClasslikes%2F1617540583" anchor-label="KA_GE" id="-1877584611%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-k-a_-g-e/index.html">KA_GE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1877584611%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-k-a_-g-e/index.html">KA_GE</a></div></div><div class="brief "><p class="paragraph">Georgian</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2038020171%2FClasslikes%2F1617540583" anchor-label="DE_DE" id="-2038020171%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-d-e_-d-e/index.html">DE_DE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2038020171%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-d-e_-d-e/index.html">DE_DE</a></div></div><div class="brief "><p class="paragraph">German</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="646127417%2FClasslikes%2F1617540583" anchor-label="EL_GR" id="646127417%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-e-l_-g-r/index.html">EL_GR</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="646127417%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-e-l_-g-r/index.html">EL_GR</a></div></div><div class="brief "><p class="paragraph">Greek</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1276231308%2FClasslikes%2F1617540583" anchor-label="GU_IN" id="1276231308%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-g-u_-i-n/index.html">GU_IN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1276231308%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-g-u_-i-n/index.html">GU_IN</a></div></div><div class="brief "><p class="paragraph">Gujarati (India)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-96985547%2FClasslikes%2F1617540583" anchor-label="HA_LATN_NG" id="-96985547%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-h-a_-l-a-t-n_-n-g/index.html">HA_LATN_NG</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-96985547%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-h-a_-l-a-t-n_-n-g/index.html">HA_LATN_NG</a></div></div><div class="brief "><p class="paragraph">Hausa - Latin (Nigeria)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="331986907%2FClasslikes%2F1617540583" anchor-label="HE_IL" id="331986907%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-h-e_-i-l/index.html">HE_IL</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="331986907%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-h-e_-i-l/index.html">HE_IL</a></div></div><div class="brief "><p class="paragraph">Hebrew</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1247801561%2FClasslikes%2F1617540583" anchor-label="HI_IN" id="1247801561%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-h-i_-i-n/index.html">HI_IN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1247801561%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-h-i_-i-n/index.html">HI_IN</a></div></div><div class="brief "><p class="paragraph">Hindi</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1922894901%2FClasslikes%2F1617540583" anchor-label="HU_HU" id="1922894901%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-h-u_-h-u/index.html">HU_HU</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1922894901%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-h-u_-h-u/index.html">HU_HU</a></div></div><div class="brief "><p class="paragraph">Hungarian</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1117418261%2FClasslikes%2F1617540583" anchor-label="IS_IS" id="1117418261%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-i-s_-i-s/index.html">IS_IS</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1117418261%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-i-s_-i-s/index.html">IS_IS</a></div></div><div class="brief "><p class="paragraph">Icelandic</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2133631334%2FClasslikes%2F1617540583" anchor-label="IG_LATN_NG" id="-2133631334%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-i-g_-l-a-t-n_-n-g/index.html">IG_LATN_NG</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2133631334%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-i-g_-l-a-t-n_-n-g/index.html">IG_LATN_NG</a></div></div><div class="brief "><p class="paragraph">Igbo - Latin (Nigera)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-687490699%2FClasslikes%2F1617540583" anchor-label="ID_ID" id="-687490699%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-i-d_-i-d/index.html">ID_ID</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-687490699%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-i-d_-i-d/index.html">ID_ID</a></div></div><div class="brief "><p class="paragraph">Indonesian (Bahasa)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1372611113%2FClasslikes%2F1617540583" anchor-label="GA_IE" id="-1372611113%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-g-a_-i-e/index.html">GA_IE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1372611113%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-g-a_-i-e/index.html">GA_IE</a></div></div><div class="brief "><p class="paragraph">Irish</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-561506718%2FClasslikes%2F1617540583" anchor-label="XH" id="-561506718%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-x-h/index.html">XH</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-561506718%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-x-h/index.html">XH</a></div></div><div class="brief "><p class="paragraph">IsiXhosa</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="396120161%2FClasslikes%2F1617540583" anchor-label="ZU_ZA" id="396120161%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-z-u_-z-a/index.html">ZU_ZA</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="396120161%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-z-u_-z-a/index.html">ZU_ZA</a></div></div><div class="brief "><p class="paragraph">IsiZulu (South Africa)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1237745525%2FClasslikes%2F1617540583" anchor-label="IT_IT" id="1237745525%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-i-t_-i-t/index.html">IT_IT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1237745525%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-i-t_-i-t/index.html">IT_IT</a></div></div><div class="brief "><p class="paragraph">Italian</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1570364356%2FClasslikes%2F1617540583" anchor-label="JA_JP" id="1570364356%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-j-a_-j-p/index.html">JA_JP</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1570364356%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-j-a_-j-p/index.html">JA_JP</a></div></div><div class="brief "><p class="paragraph">Japanese</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-29090633%2FClasslikes%2F1617540583" anchor-label="KN_IN" id="-29090633%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-k-n_-i-n/index.html">KN_IN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-29090633%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-k-n_-i-n/index.html">KN_IN</a></div></div><div class="brief "><p class="paragraph">Kannada (India)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2086152412%2FClasslikes%2F1617540583" anchor-label="KK_KZ" id="-2086152412%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-k-k_-k-z/index.html">KK_KZ</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2086152412%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-k-k_-k-z/index.html">KK_KZ</a></div></div><div class="brief "><p class="paragraph">Kazakh</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1795409200%2FClasslikes%2F1617540583" anchor-label="KM_KH" id="-1795409200%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-k-m_-k-h/index.html">KM_KH</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1795409200%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-k-m_-k-h/index.html">KM_KH</a></div></div><div class="brief "><p class="paragraph">Khmer (Cambodia)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="191868819%2FClasslikes%2F1617540583" anchor-label="QUC_LATN_GT" id="191868819%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-q-u-c_-l-a-t-n_-g-t/index.html">QUC_LATN_GT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="191868819%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-q-u-c_-l-a-t-n_-g-t/index.html">QUC_LATN_GT</a></div></div><div class="brief "><p class="paragraph">K'iche' - Latin (Guatemala)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="810295605%2FClasslikes%2F1617540583" anchor-label="RW_RW" id="810295605%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-r-w_-r-w/index.html">RW_RW</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="810295605%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-r-w_-r-w/index.html">RW_RW</a></div></div><div class="brief "><p class="paragraph">Kinyarwanda (Rwanda)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-210885930%2FClasslikes%2F1617540583" anchor-label="SW" id="-210885930%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-w/index.html">SW</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-210885930%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-s-w/index.html">SW</a></div></div><div class="brief "><p class="paragraph">KiSwahili</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-114919249%2FClasslikes%2F1617540583" anchor-label="KOK_IN" id="-114919249%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-k-o-k_-i-n/index.html">KOK_IN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-114919249%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-k-o-k_-i-n/index.html">KOK_IN</a></div></div><div class="brief "><p class="paragraph">Konkani (India)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1002190232%2FClasslikes%2F1617540583" anchor-label="KO_KR" id="1002190232%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-k-o_-k-r/index.html">KO_KR</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1002190232%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-k-o_-k-r/index.html">KO_KR</a></div></div><div class="brief "><p class="paragraph">Korean</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="567041260%2FClasslikes%2F1617540583" anchor-label="KY_CYRL_KG" id="567041260%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-k-y_-c-y-r-l_-k-g/index.html">KY_CYRL_KG</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="567041260%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-k-y_-c-y-r-l_-k-g/index.html">KY_CYRL_KG</a></div></div><div class="brief "><p class="paragraph">Kyrgyz - Cyrillic</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-216066283%2FClasslikes%2F1617540583" anchor-label="LV_LV" id="-216066283%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-l-v_-l-v/index.html">LV_LV</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-216066283%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-l-v_-l-v/index.html">LV_LV</a></div></div><div class="brief "><p class="paragraph">Latvian</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-456720811%2FClasslikes%2F1617540583" anchor-label="LT_LT" id="-456720811%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-l-t_-l-t/index.html">LT_LT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-456720811%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-l-t_-l-t/index.html">LT_LT</a></div></div><div class="brief "><p class="paragraph">Lithuanian</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-307963800%2FClasslikes%2F1617540583" anchor-label="LB_LU" id="-307963800%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-l-b_-l-u/index.html">LB_LU</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-307963800%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-l-b_-l-u/index.html">LB_LU</a></div></div><div class="brief "><p class="paragraph">Luxembourgish</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2104488299%2FClasslikes%2F1617540583" anchor-label="MK_MK" id="-2104488299%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-m-k_-m-k/index.html">MK_MK</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2104488299%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-m-k_-m-k/index.html">MK_MK</a></div></div><div class="brief "><p class="paragraph">Macedonian</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1849580315%2FClasslikes%2F1617540583" anchor-label="MS_MY" id="1849580315%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-m-s_-m-y/index.html">MS_MY</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1849580315%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-m-s_-m-y/index.html">MS_MY</a></div></div><div class="brief "><p class="paragraph">Malay (Bahasa)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1249123333%2FClasslikes%2F1617540583" anchor-label="ML_IN" id="-1249123333%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-m-l_-i-n/index.html">ML_IN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1249123333%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-m-l_-i-n/index.html">ML_IN</a></div></div><div class="brief "><p class="paragraph">Malayalam (India)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1021542923%2FClasslikes%2F1617540583" anchor-label="MT_MT" id="-1021542923%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-m-t_-m-t/index.html">MT_MT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1021542923%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-m-t_-m-t/index.html">MT_MT</a></div></div><div class="brief "><p class="paragraph">Maltese  (Malta)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1879219861%2FClasslikes%2F1617540583" anchor-label="MI_LATN_NZ" id="-1879219861%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-m-i_-l-a-t-n_-n-z/index.html">MI_LATN_NZ</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1879219861%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-m-i_-l-a-t-n_-n-z/index.html">MI_LATN_NZ</a></div></div><div class="brief "><p class="paragraph">Maori - Latin (New Zealand)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="776357045%2FClasslikes%2F1617540583" anchor-label="MR_IN" id="776357045%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-m-r_-i-n/index.html">MR_IN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="776357045%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-m-r_-i-n/index.html">MR_IN</a></div></div><div class="brief "><p class="paragraph">Marathi (India)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-224921500%2FClasslikes%2F1617540583" anchor-label="MN_CYRL_MN" id="-224921500%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-m-n_-c-y-r-l_-m-n/index.html">MN_CYRL_MN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-224921500%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-m-n_-c-y-r-l_-m-n/index.html">MN_CYRL_MN</a></div></div><div class="brief "><p class="paragraph">Mongolian - Cyrillic</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="661396160%2FClasslikes%2F1617540583" anchor-label="NE_NP" id="661396160%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-n-e_-n-p/index.html">NE_NP</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="661396160%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-n-e_-n-p/index.html">NE_NP</a></div></div><div class="brief "><p class="paragraph">Nepali (Nepal)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-134091230%2FClasslikes%2F1617540583" anchor-label="NB_NO" id="-134091230%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-n-b_-n-o/index.html">NB_NO</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-134091230%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-n-b_-n-o/index.html">NB_NO</a></div></div><div class="brief "><p class="paragraph">Norwegian (Bokmal)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-378097770%2FClasslikes%2F1617540583" anchor-label="NN_NO" id="-378097770%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-n-n_-n-o/index.html">NN_NO</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-378097770%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-n-n_-n-o/index.html">NN_NO</a></div></div><div class="brief "><p class="paragraph">Norwegian (Nynorsk)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="231484471%2FClasslikes%2F1617540583" anchor-label="OR_IN" id="231484471%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-o-r_-i-n/index.html">OR_IN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="231484471%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-o-r_-i-n/index.html">OR_IN</a></div></div><div class="brief "><p class="paragraph">Odia (India)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="616339925%2FClasslikes%2F1617540583" anchor-label="PL_PL" id="616339925%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-p-l_-p-l/index.html">PL_PL</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="616339925%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-p-l_-p-l/index.html">PL_PL</a></div></div><div class="brief "><p class="paragraph">Polish</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1811897889%2FClasslikes%2F1617540583" anchor-label="PT_BR" id="1811897889%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-p-t_-b-r/index.html">PT_BR</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1811897889%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-p-t_-b-r/index.html">PT_BR</a></div></div><div class="brief "><p class="paragraph">Portuguese (Brazil)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1578958037%2FClasslikes%2F1617540583" anchor-label="PT_PT" id="1578958037%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-p-t_-p-t/index.html">PT_PT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1578958037%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-p-t_-p-t/index.html">PT_PT</a></div></div><div class="brief "><p class="paragraph">Portuguese (Portugal)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="910150517%2FClasslikes%2F1617540583" anchor-label="PA_GURU" id="910150517%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-p-a_-g-u-r-u/index.html">PA_GURU</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="910150517%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-p-a_-g-u-r-u/index.html">PA_GURU</a></div></div><div class="brief "><p class="paragraph">Punjabi - Gurmukhi</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1332307946%2FClasslikes%2F1617540583" anchor-label="PA_ARAB" id="-1332307946%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-p-a_-a-r-a-b/index.html">PA_ARAB</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1332307946%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-p-a_-a-r-a-b/index.html">PA_ARAB</a></div></div><div class="brief "><p class="paragraph">Punjabi - Arabic</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="590398044%2FClasslikes%2F1617540583" anchor-label="QU_LATN_PE" id="590398044%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-q-u_-l-a-t-n_-p-e/index.html">QU_LATN_PE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="590398044%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-q-u_-l-a-t-n_-p-e/index.html">QU_LATN_PE</a></div></div><div class="brief "><p class="paragraph">Quechua - Latin (Peru)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-152322507%2FClasslikes%2F1617540583" anchor-label="RO_RO" id="-152322507%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-r-o_-r-o/index.html">RO_RO</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-152322507%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-r-o_-r-o/index.html">RO_RO</a></div></div><div class="brief "><p class="paragraph">Romanian</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="569641077%2FClasslikes%2F1617540583" anchor-label="RU_RU" id="569641077%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-r-u_-r-u/index.html">RU_RU</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="569641077%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-r-u_-r-u/index.html">RU_RU</a></div></div><div class="brief "><p class="paragraph">Russian</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1516985669%2FClasslikes%2F1617540583" anchor-label="GD_LATN_GB" id="-1516985669%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-g-d_-l-a-t-n_-g-b/index.html">GD_LATN_GB</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1516985669%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-g-d_-l-a-t-n_-g-b/index.html">GD_LATN_GB</a></div></div><div class="brief "><p class="paragraph">Scottish Gaelic - Latin</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-870235968%2FClasslikes%2F1617540583" anchor-label="SR_CYRL_BA" id="-870235968%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-r_-c-y-r-l_-b-a/index.html">SR_CYRL_BA</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-870235968%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-s-r_-c-y-r-l_-b-a/index.html">SR_CYRL_BA</a></div></div><div class="brief "><p class="paragraph">Serbian - Cyrillic (Bosnia)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-869024958%2FClasslikes%2F1617540583" anchor-label="SR_CYRL_RS" id="-869024958%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-r_-c-y-r-l_-r-s/index.html">SR_CYRL_RS</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-869024958%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-s-r_-c-y-r-l_-r-s/index.html">SR_CYRL_RS</a></div></div><div class="brief "><p class="paragraph">Serbian - Cyrillic (Serbia)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1725996451%2FClasslikes%2F1617540583" anchor-label="SR_LATN_RS" id="1725996451%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-r_-l-a-t-n_-r-s/index.html">SR_LATN_RS</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1725996451%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-s-r_-l-a-t-n_-r-s/index.html">SR_LATN_RS</a></div></div><div class="brief "><p class="paragraph">Serbian - Latin (Serbia)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="580095950%2FClasslikes%2F1617540583" anchor-label="NSO_ZA" id="580095950%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-n-s-o_-z-a/index.html">NSO_ZA</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="580095950%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-n-s-o_-z-a/index.html">NSO_ZA</a></div></div><div class="brief "><p class="paragraph">Sesotho Sa Leboa (South Africa)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-695480212%2FClasslikes%2F1617540583" anchor-label="TN" id="-695480212%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-t-n/index.html">TN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-695480212%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-t-n/index.html">TN</a></div></div><div class="brief "><p class="paragraph">Setswana</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-353879114%2FClasslikes%2F1617540583" anchor-label="SD_ARAB" id="-353879114%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-d_-a-r-a-b/index.html">SD_ARAB</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-353879114%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-s-d_-a-r-a-b/index.html">SD_ARAB</a></div></div><div class="brief "><p class="paragraph">Sindhi - Arabic</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="173086974%2FClasslikes%2F1617540583" anchor-label="SI_LK" id="173086974%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-i_-l-k/index.html">SI_LK</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="173086974%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-s-i_-l-k/index.html">SI_LK</a></div></div><div class="brief "><p class="paragraph">Sinhala (Sri Lanka)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1198453675%2FClasslikes%2F1617540583" anchor-label="SK_SK" id="-1198453675%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-k_-s-k/index.html">SK_SK</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1198453675%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-s-k_-s-k/index.html">SK_SK</a></div></div><div class="brief "><p class="paragraph">Slovak</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1721115634%2FClasslikes%2F1617540583" anchor-label="SL_SI" id="1721115634%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-l_-s-i/index.html">SL_SI</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1721115634%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-s-l_-s-i/index.html">SL_SI</a></div></div><div class="brief "><p class="paragraph">Slovenian</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1678948136%2FClasslikes%2F1617540583" anchor-label="ES_AR" id="-1678948136%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-e-s_-a-r/index.html">ES_AR</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1678948136%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-e-s_-a-r/index.html">ES_AR</a></div></div><div class="brief "><p class="paragraph">Spanish (Argentina)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2098839762%2FClasslikes%2F1617540583" anchor-label="ES_MX" id="2098839762%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-e-s_-m-x/index.html">ES_MX</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2098839762%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-e-s_-m-x/index.html">ES_MX</a></div></div><div class="brief "><p class="paragraph">Spanish (Mexico)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-918260587%2FClasslikes%2F1617540583" anchor-label="ES_ES" id="-918260587%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-e-s_-e-s/index.html">ES_ES</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-918260587%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-e-s_-e-s/index.html">ES_ES</a></div></div><div class="brief "><p class="paragraph">Spanish (Spain)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1670960164%2FClasslikes%2F1617540583" anchor-label="SV_SE" id="1670960164%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-v_-s-e/index.html">SV_SE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1670960164%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-s-v_-s-e/index.html">SV_SE</a></div></div><div class="brief "><p class="paragraph">Swedish</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-541370933%2FClasslikes%2F1617540583" anchor-label="TG_CYRL_TJ" id="-541370933%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-t-g_-c-y-r-l_-t-j/index.html">TG_CYRL_TJ</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-541370933%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-t-g_-c-y-r-l_-t-j/index.html">TG_CYRL_TJ</a></div></div><div class="brief "><p class="paragraph">Tajik - Cyrillic</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-18677473%2FClasslikes%2F1617540583" anchor-label="TA" id="-18677473%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-t-a/index.html">TA</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-18677473%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-t-a/index.html">TA</a></div></div><div class="brief "><p class="paragraph">Tamil</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1843116251%2FClasslikes%2F1617540583" anchor-label="TT_CYRL_RU" id="-1843116251%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-t-t_-c-y-r-l_-r-u/index.html">TT_CYRL_RU</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1843116251%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-t-t_-c-y-r-l_-r-u/index.html">TT_CYRL_RU</a></div></div><div class="brief "><p class="paragraph">Tatar - Cyrillic (Russia)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="923213161%2FClasslikes%2F1617540583" anchor-label="TE_IN" id="923213161%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-t-e_-i-n/index.html">TE_IN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="923213161%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-t-e_-i-n/index.html">TE_IN</a></div></div><div class="brief "><p class="paragraph">Telugu (India)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2124257579%2FClasslikes%2F1617540583" anchor-label="TH_TH" id="-2124257579%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-t-h_-t-h/index.html">TH_TH</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2124257579%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-t-h_-t-h/index.html">TH_TH</a></div></div><div class="brief "><p class="paragraph">Thai</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2139559919%2FClasslikes%2F1617540583" anchor-label="TI_ET" id="2139559919%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-t-i_-e-t/index.html">TI_ET</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2139559919%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-t-i_-e-t/index.html">TI_ET</a></div></div><div class="brief "><p class="paragraph">Tigrinya (Ethiopia)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-920984939%2FClasslikes%2F1617540583" anchor-label="TR_TR" id="-920984939%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-t-r_-t-r/index.html">TR_TR</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-920984939%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-t-r_-t-r/index.html">TR_TR</a></div></div><div class="brief "><p class="paragraph">Turkish</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2052315635%2FClasslikes%2F1617540583" anchor-label="TK_LATN_TM" id="2052315635%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-t-k_-l-a-t-n_-t-m/index.html">TK_LATN_TM</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2052315635%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-t-k_-l-a-t-n_-t-m/index.html">TK_LATN_TM</a></div></div><div class="brief "><p class="paragraph">Turkmen - Latin</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-155569909%2FClasslikes%2F1617540583" anchor-label="UK_UA" id="-155569909%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-u-k_-u-a/index.html">UK_UA</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-155569909%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-u-k_-u-a/index.html">UK_UA</a></div></div><div class="brief "><p class="paragraph">Ukrainian</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1856877233%2FClasslikes%2F1617540583" anchor-label="UR" id="-1856877233%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-u-r/index.html">UR</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1856877233%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-u-r/index.html">UR</a></div></div><div class="brief "><p class="paragraph">Urdu</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="442816469%2FClasslikes%2F1617540583" anchor-label="UG_ARAB" id="442816469%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-u-g_-a-r-a-b/index.html">UG_ARAB</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="442816469%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-u-g_-a-r-a-b/index.html">UG_ARAB</a></div></div><div class="brief "><p class="paragraph">Uyghur - Arabic</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="599267436%2FClasslikes%2F1617540583" anchor-label="UZ_CYRL_UZ" id="599267436%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-u-z_-c-y-r-l_-u-z/index.html">UZ_CYRL_UZ</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="599267436%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-u-z_-c-y-r-l_-u-z/index.html">UZ_CYRL_UZ</a></div></div><div class="brief "><p class="paragraph">Uzbek - Cyrillic</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1100678451%2FClasslikes%2F1617540583" anchor-label="UZ_LATN_UZ" id="-1100678451%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-u-z_-l-a-t-n_-u-z/index.html">UZ_LATN_UZ</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1100678451%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-u-z_-l-a-t-n_-u-z/index.html">UZ_LATN_UZ</a></div></div><div class="brief "><p class="paragraph">Uzbek - Latin</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1370443785%2FClasslikes%2F1617540583" anchor-label="CAT_ES" id="1370443785%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-c-a-t_-e-s/index.html">CAT_ES</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1370443785%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-c-a-t_-e-s/index.html">CAT_ES</a></div></div><div class="brief "><p class="paragraph">Valencian (Spain)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2072354886%2FClasslikes%2F1617540583" anchor-label="VI_VN" id="-2072354886%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-v-i_-v-n/index.html">VI_VN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2072354886%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-v-i_-v-n/index.html">VI_VN</a></div></div><div class="brief "><p class="paragraph">Vietnamese</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1681832646%2FClasslikes%2F1617540583" anchor-label="CY_GB" id="-1681832646%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-c-y_-g-b/index.html">CY_GB</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1681832646%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-c-y_-g-b/index.html">CY_GB</a></div></div><div class="brief "><p class="paragraph">Welsh</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-871432276%2FClasslikes%2F1617540583" anchor-label="WO_LATN" id="-871432276%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-w-o_-l-a-t-n/index.html">WO_LATN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-871432276%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-w-o_-l-a-t-n/index.html">WO_LATN</a></div></div><div class="brief "><p class="paragraph">Wolof - Latin</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-507965778%2FClasslikes%2F1617540583" anchor-label="YO_LATN" id="-507965778%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-y-o_-l-a-t-n/index.html">YO_LATN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-507965778%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-y-o_-l-a-t-n/index.html">YO_LATN</a></div></div><div class="brief "><p class="paragraph">Yoruba - Latin</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="1301402892%2FProperties%2F1617540583" anchor-label="entries" id="1301402892%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="entries.html"><span><span>entries</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1301402892%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="entries.html">entries</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html">EnumEntries</a><span class="token operator">&lt;</span><a href="index.html">LanguageCode</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Returns a representation of an immutable list of all enum entries, in the order they're declared.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1785250571%2FProperties%2F1617540583" anchor-label="value" id="1785250571%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="value.html"><span><span>value</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1785250571%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="value.html">value</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="587308048%2FFunctions%2F1617540583" anchor-label="valueOf" id="587308048%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="value-of.html"><span>value</span><wbr></wbr><span><span>Of</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="587308048%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><a href="value-of.html"><span class="token function">valueOf</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">value<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">LanguageCode</a></div><div class="brief "><p class="paragraph">Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1074447644%2FFunctions%2F1617540583" anchor-label="values" id="1074447644%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="values.html"><span><span>values</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1074447644%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><a href="values.html"><span class="token function">values</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="token operator">&lt;</span><a href="index.html">LanguageCode</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Returns an array containing the constants of this enum type, in the order they're declared.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
    <div class="footer">
        <a href="#content" id="go-to-top-link" class="footer--button footer--button_go-to-top"></a>
        <span>© 2026 Copyright</span>
        <span class="pull-right">
            <span>Generated by </span>
            <a class="footer--link footer--link_external" href="https://github.com/Kotlin/dokka">
                <span>dokka</span>
            </a>
        </span>
    </div>
            </div>
        </div>
    </div>
</body>
</html>
</div>
`
}</HTMLBlock>
