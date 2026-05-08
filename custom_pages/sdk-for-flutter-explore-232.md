---
title: "com.here.sdk.core"
slug: "sdk-for-flutter-explore"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>com.here.sdk.core</title>
    <link href="../../images/logo-icon.svg" rel="icon" type="image/svg">
    <script>var pathToRoot = "../../";</script>
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
<script type="text/javascript" src="../../scripts/sourceset_dependencies.js" async="async"></script>
<link href="../../styles/style.css" rel="Stylesheet">
<link href="../../styles/main.css" rel="Stylesheet">
<link href="../../styles/prism.css" rel="Stylesheet">
<link href="../../styles/logo-styles.css" rel="Stylesheet">
<link href="../../styles/font-jb-sans-auto.css" rel="Stylesheet">
<link href="../../ui-kit/ui-kit.min.css" rel="Stylesheet">
<script type="text/javascript" src="../../scripts/clipboard.js" async="async"></script>
<script type="text/javascript" src="../../scripts/navigation-loader.js" async="async"></script>
<script type="text/javascript" src="../../scripts/platform-content-handler.js" async="async"></script>
<script type="text/javascript" src="../../scripts/main.js" defer="defer"></script>
<script type="text/javascript" src="../../scripts/prism.js" async="async"></script>
<script type="text/javascript" src="../../ui-kit/ui-kit.min.js" defer="defer"></script>
<script type="text/javascript" src="../../scripts/symbol-parameters-wrapper_deferred.js" defer="defer"></script>
</head>
<body>
    <div class="root">
    <nav class="navigation theme-dark" id="navigation-wrapper">
            <a class="library-name--link" href="sdk-for-flutter-explore-index">
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
<div class="main-content" data-page-type="package" id="content" pageIds="API Reference::com.here.sdk.core////PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><span class="current">com.here.sdk.core</span></div>
  <div class="cover ">
    <h1 class="cover"><span><span>Package-level</span></span> <span><span>declarations</span></span></h1>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="TYPE">Types</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="1351803967%2FClasslikes%2F1617540583" anchor-label="Anchor2D" id="1351803967%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span><span>Anchor2D</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1351803967%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">Anchor2D</a></div><div class="brief "><p class="paragraph">Represents a point in a rectangle as a ratio of this rectangle's width and height.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1382247657%2FClasslikes%2F1617540583" anchor-label="Angle" id="1382247657%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span><span>Angle</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1382247657%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">Angle</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a></div><div class="brief "><p class="paragraph">Represents an angle independent of the unit of measurement.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1550578684%2FClasslikes%2F1617540583" anchor-label="AngleRange" id="1550578684%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Angle</span><wbr></wbr><span><span>Range</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1550578684%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">AngleRange</a></div><div class="brief "><p class="paragraph">Represents angle ranges as a circular sector by using an absolute start angle and a relative range angle called extent. They both define a sector on a circle. All angles are in degrees and are clockwise-oriented. By default, the AngleRange represents the entire circle, the value is in the range of \[0, 360\]. Values will be corrected during construction using normalization for the start angle and clamping for the extent angle, ensuring a valid range for all possible inputs.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-436592914%2FClasslikes%2F1617540583" anchor-label="Authentication" id="-436592914%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span><span>Authentication</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-436592914%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">Authentication</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a></div><div class="brief "><p class="paragraph">Use the authentication class to authenticate and retrieve a secure token that can be used with other HERE services.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-117712599%2FClasslikes%2F1617540583" anchor-label="AuthenticationCallback" id="-117712599%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Authentication</span><wbr></wbr><span><span>Callback</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-117712599%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">AuthenticationCallback</a></div><div class="brief "><p class="paragraph">Callback passed to <a href="sdk-for-flutter-explore-authenticate">com.here.sdk.core.Authentication.authenticate</a>. This callback is called on the main thread asynchronously when an authenticate call has completed.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="935201764%2FClasslikes%2F1617540583" anchor-label="AuthenticationData" id="935201764%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Authentication</span><wbr></wbr><span><span>Data</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="935201764%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">AuthenticationData</a></div><div class="brief "><p class="paragraph">Authentication data</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1189343572%2FClasslikes%2F1617540583" anchor-label="AuthenticationError" id="-1189343572%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Authentication</span><wbr></wbr><span><span>Error</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1189343572%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">AuthenticationError</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">AuthenticationError</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Authentication error</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="696673477%2FClasslikes%2F1617540583" anchor-label="AuthenticationException" id="696673477%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Authentication</span><wbr></wbr><span><span>Exception</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="696673477%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">AuthenticationException</a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span class="token keyword">val </span>error<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">AuthenticationError</a></span></span><span class="token punctuation">)</span> : <a href="https://developer.android.com/reference/kotlin/java/lang/Exception.html">Exception</a></div><div class="brief "><p class="paragraph">Authentication exception</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1706965834%2FClasslikes%2F1617540583" anchor-label="BrandLogo" id="1706965834%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Brand</span><wbr></wbr><span><span>Logo</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1706965834%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">BrandLogo</a></div><div class="brief "><p class="paragraph">Represents image link to the company's logo. <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="47389309%2FClasslikes%2F1617540583" anchor-label="CardinalDirection" id="47389309%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Cardinal</span><wbr></wbr><span><span>Direction</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="47389309%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">CardinalDirection</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">CardinalDirection</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Indicates the official directional identifier assigned to this road. The direction indicates the same information as on the signpost shield text: For example, if it is &quot;101 West&quot;, the direction contains WEST.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-182568871%2FClasslikes%2F1617540583" anchor-label="Color" id="-182568871%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span><span>Color</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-182568871%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">Color</a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">fred<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html">Float</a><span class="token punctuation">, </span></span><span class="parameter ">fgreen<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html">Float</a><span class="token punctuation">, </span></span><span class="parameter ">fblue<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html">Float</a><span class="token punctuation">, </span></span><span class="parameter ">falpha<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html">Float</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Represents a color value.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1173994279%2FClasslikes%2F1617540583" anchor-label="CountryCode" id="-1173994279%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Country</span><wbr></wbr><span><span>Code</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1173994279%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">CountryCode</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">CountryCode</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">This enum represents country codes in accordance with the ISO 3166-1 standard using alpha-3 codes.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-410424023%2FClasslikes%2F1617540583" anchor-label="CurrentType" id="-410424023%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Current</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-410424023%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">CurrentType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">CurrentType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">This enum represents the type of electric current</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1010900821%2FClasslikes%2F1617540583" anchor-label="CustomMetadataValue" id="-1010900821%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Custom</span><wbr></wbr><span>Metadata</span><wbr></wbr><span><span>Value</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1010900821%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">CustomMetadataValue</a></div><div class="brief "><p class="paragraph">Interface for storing arbitrary metadata types. By implementing this interface, multiple object types can be stored as desired, simply by adding fields to the implementation that refer to those objects and then assigning an instance of the CustomMetadataValue derived class to a map item.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1379835264%2FClasslikes%2F1617540583" anchor-label="ExternalID" id="1379835264%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>External</span><wbr></wbr><span><span>ID</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1379835264%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">ExternalID</a></div><div class="brief "><p class="paragraph">Identifier of the entity as provided by the external source</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2067024876%2FClasslikes%2F1617540583" anchor-label="GeoBox" id="2067024876%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Geo</span><wbr></wbr><span><span>Box</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2067024876%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">GeoBox</a></div><div class="brief "><p class="paragraph">Represents a bounding rectangle aligned with latitude and longitude. Geographic area represented by this would be visualised as a rectangle when using a normal cylindrical projection (such as Mercator). The box has a maximum span of 360 degrees in longitude and 180 degrees in latitude direction. The box with equal values in longitude for the corners is considered as a span of 360 degrees. The box is considered empty if the latitude of the <a href="sdk-for-flutter-explore-south-west-corner">com.here.sdk.core.GeoBox.southWestCorner</a> is larger than the the latitude of the <a href="sdk-for-flutter-explore-north-east-corner">com.here.sdk.core.GeoBox.northEastCorner</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="175726715%2FClasslikes%2F1617540583" anchor-label="GeoCircle" id="175726715%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Geo</span><wbr></wbr><span><span>Circle</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="175726715%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">GeoCircle</a></div><div class="brief "><p class="paragraph">Represents a circle area in 2D space.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1900208196%2FClasslikes%2F1617540583" anchor-label="GeoCoordinates" id="-1900208196%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Geo</span><wbr></wbr><span><span>Coordinates</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1900208196%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a></div><div class="brief "><p class="paragraph">Represents geographical coordinates in 3D space.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-109277517%2FClasslikes%2F1617540583" anchor-label="GeoCoordinatesUpdate" id="-109277517%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Geo</span><wbr></wbr><span>Coordinates</span><wbr></wbr><span><span>Update</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-109277517%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">GeoCoordinatesUpdate</a></div><div class="brief "><p class="paragraph">Represents geographical coordinates in 3D space. Unlike <a href="sdk-for-flutter-explore-index">com.here.sdk.core.GeoCoordinates</a>, its members can be undefined, allowing for APIs that update only the specified parts of geo coordinates.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1639180767%2FClasslikes%2F1617540583" anchor-label="GeoCorridor" id="-1639180767%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Geo</span><wbr></wbr><span><span>Corridor</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1639180767%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">GeoCorridor</a></div><div class="brief "><p class="paragraph">A geographical area that wraps around a geographical polyline with a given distance. The corridor has round edges at the endpoints of the polyline. The distance from any point of the polyline to the closest border of the corridor is always the same.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2122837383%2FClasslikes%2F1617540583" anchor-label="GeoOrientation" id="2122837383%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Geo</span><wbr></wbr><span><span>Orientation</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2122837383%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">GeoOrientation</a></div><div class="brief "><p class="paragraph">Geodetic orientation with bearing, tilt and roll.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1177905090%2FClasslikes%2F1617540583" anchor-label="GeoOrientationUpdate" id="-1177905090%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Geo</span><wbr></wbr><span>Orientation</span><wbr></wbr><span><span>Update</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1177905090%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">GeoOrientationUpdate</a></div><div class="brief "><p class="paragraph">Describes geodetic orientation update with bearing and tilt. Updating an orientation value can be skipped by setting <code class="lang-kotlin">null</code> in an appriopriate field. For example, if one wants bearing not to be updated set it to <code class="lang-kotlin">null</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1335010211%2FClasslikes%2F1617540583" anchor-label="GeoPolygon" id="-1335010211%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Geo</span><wbr></wbr><span><span>Polygon</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1335010211%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">GeoPolygon</a></div><div class="brief "><p class="paragraph">Represents a <code class="lang-kotlin">GeoPolygon</code> area as a series of geographic coordinates, and optionally, a list of inner boundaries (also known as holes). An instance of this class, initialized with appropriate vertices.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1747921675%2FClasslikes%2F1617540583" anchor-label="GeoPolyline" id="1747921675%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Geo</span><wbr></wbr><span><span>Polyline</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1747921675%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">GeoPolyline</a></div><div class="brief "><p class="paragraph">A list of geographic coordinates representing the vertices of a polyline. An instance of this class, initialized with appropriate vertices. Represents a <code class="lang-kotlin">GeoPolyline</code> as a series of geographic coordinates.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-975443944%2FClasslikes%2F1617540583" anchor-label="GeoPolylineDirection" id="-975443944%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Geo</span><wbr></wbr><span>Polyline</span><wbr></wbr><span><span>Direction</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-975443944%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">GeoPolylineDirection</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">GeoPolylineDirection</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Defines if a function on a <a href="sdk-for-flutter-explore-index">com.here.sdk.core.GeoPolyline</a> computes the operation starting from the beginning or from the end of <a href="sdk-for-flutter-explore-vertices">com.here.sdk.core.GeoPolyline.vertices</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1635133977%2FClasslikes%2F1617540583" anchor-label="IntegerRange" id="-1635133977%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Integer</span><wbr></wbr><span><span>Range</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1635133977%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">IntegerRange</a></div><div class="brief "><p class="paragraph">An integer range \[min, max\] with inclusive minimum and maximum value.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1490220513%2FClasslikes%2F1617540583" anchor-label="LanguageCode" id="1490220513%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Language</span><wbr></wbr><span><span>Code</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1490220513%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">LanguageCode</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">LanguageCode</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">This enum represents language codes. The basic naming pattern consists of a 2-letter ISO 639-1 language code followed by a 2-letter ISO 3166-1 country code. Some language codes consist only of a language code, i.e. without a country code. When there is no ISO 639-1 language code, the related ISO 639-2 or ISO 639-3 language code is used. In case the script is specified, its ISO 15924 code is used.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="986710292%2FClasslikes%2F1617540583" anchor-label="LocalizedText" id="986710292%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Localized</span><wbr></wbr><span><span>Text</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="986710292%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">LocalizedText</a></div><div class="brief "><p class="paragraph">Used to represent text localized to specific language.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="442130075%2FClasslikes%2F1617540583" anchor-label="LocalizedTexts" id="442130075%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Localized</span><wbr></wbr><span><span>Texts</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="442130075%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">LocalizedTexts</a></div><div class="brief "><p class="paragraph">The list of multiple names or titles for the same entity, possibly in different languages.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1988207599%2FClasslikes%2F1617540583" anchor-label="Location" id="-1988207599%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span><span>Location</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1988207599%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">Location</a></div><div class="brief "><p class="paragraph">Describes a location in the world at a given time.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-397858371%2FClasslikes%2F1617540583" anchor-label="LocationListener" id="-397858371%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Location</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-397858371%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">LocationListener</a></div><div class="brief "><p class="paragraph">This interface should be implemented in order to receive notifications about location updates.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1763821622%2FClasslikes%2F1617540583" anchor-label="LocationSource" id="1763821622%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Location</span><wbr></wbr><span><span>Source</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1763821622%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">LocationSource</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">LocationSource</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Indicates where the location was computed.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-916943771%2FClasslikes%2F1617540583" anchor-label="LocationTechnology" id="-916943771%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Location</span><wbr></wbr><span><span>Technology</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-916943771%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">LocationTechnology</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">LocationTechnology</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Technology or provider of the location.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1753045444%2FClasslikes%2F1617540583" anchor-label="LocationTime" id="1753045444%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Location</span><wbr></wbr><span><span>Time</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1753045444%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">LocationTime</a></div><div class="brief "><p class="paragraph">This struct presents all the time data tied to a location, like an arrival or departure time. The time data is originally specified in RFC 3339, section 5.6 format. For example, &quot;2022-03-23T16:07:31+01:00&quot; in Cracow, Poland, i.e. a Central European Time (CET) location. Note that this struct doesn't give any data on the tied location. The location should be derived from the context.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="65961431%2FClasslikes%2F1617540583" anchor-label="Metadata" id="65961431%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span><span>Metadata</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="65961431%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">Metadata</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a></div><div class="brief "><p class="paragraph">Holds metadata on behalf of a map item. An instance of this class can contain metadata items of varying types, such as String, Integer, Double, GeoCoordinates etc. and can also hold arbitrary metadata types by the use of the CustomMetadataValue interface.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1075916611%2FClasslikes%2F1617540583" anchor-label="MetadataType" id="-1075916611%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Metadata</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1075916611%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">MetadataType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">MetadataType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Different types of objects that can be stored in a Metadata class instance.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1029312192%2FClasslikes%2F1617540583" anchor-label="NameID" id="-1029312192%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Name</span><wbr></wbr><span><span>ID</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1029312192%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">NameID</a></div><div class="brief "><p class="paragraph">Structure to represent name-id pairs.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1877807079%2FClasslikes%2F1617540583" anchor-label="NetworkEndpoint" id="-1877807079%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Network</span><wbr></wbr><span><span>Endpoint</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1877807079%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">NetworkEndpoint</a></div><div class="brief "><p class="paragraph">Network endpoint.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1043019207%2FClasslikes%2F1617540583" anchor-label="ParameterConfiguration" id="-1043019207%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Parameter</span><wbr></wbr><span><span>Configuration</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1043019207%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">ParameterConfiguration</a></div><div class="brief "><p class="paragraph">Contains values of configurable parameters that are used in SDK. This is a BETA feature and thus there can be bugs and unexpected behavior.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-972892242%2FClasslikes%2F1617540583" anchor-label="PedestrianProfile" id="-972892242%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Pedestrian</span><wbr></wbr><span><span>Profile</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-972892242%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index"><strike>PedestrianProfile</strike></a></div><div class="brief "><p class="paragraph">Contains values of pedestrian profile. This is a BETA feature and thus there can be bugs and unexpected behavior.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1882888085%2FClasslikes%2F1617540583" anchor-label="PickedPlace" id="1882888085%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Picked</span><wbr></wbr><span><span>Place</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1882888085%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">PickedPlace</a></div><div class="brief "><p class="paragraph">Carries the result of picking a Carto POI (point of interest) object.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1207766522%2FClasslikes%2F1617540583" anchor-label="Point2D" id="1207766522%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span><span>Point2D</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1207766522%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">Point2D</a></div><div class="brief "><p class="paragraph">Represents a point in 2D space. When this point is used to indicate coordinates on a view, then (0,0) will mark the top-left corner of the view.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2125586757%2FClasslikes%2F1617540583" anchor-label="Point3D" id="-2125586757%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span><span>Point3D</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2125586757%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">Point3D</a></div><div class="brief "><p class="paragraph">Represents a point in 3D space.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="106396790%2FClasslikes%2F1617540583" anchor-label="PolylineSimplificationCallback" id="106396790%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Polyline</span><wbr></wbr><span>Simplification</span><wbr></wbr><span><span>Callback</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="106396790%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">PolylineSimplificationCallback</a></div><div class="brief "><p class="paragraph">The method will be called on the main thread when <a href="sdk-for-flutter-explore-simplify">com.here.sdk.core.PolylineSimplifier.simplify</a> is finished.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="660797055%2FClasslikes%2F1617540583" anchor-label="PolylineSimplificationError" id="660797055%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Polyline</span><wbr></wbr><span>Simplification</span><wbr></wbr><span><span>Error</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="660797055%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">PolylineSimplificationError</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">PolylineSimplificationError</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Error code which specifies, what went wrong during <a href="sdk-for-flutter-explore-simplify">com.here.sdk.core.PolylineSimplifier.simplify</a> operation.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2017786208%2FClasslikes%2F1617540583" anchor-label="PolylineSimplifier" id="2017786208%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Polyline</span><wbr></wbr><span><span>Simplifier</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2017786208%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">PolylineSimplifier</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a></div><div class="brief "><p class="paragraph">PolylineSimplifier helps to reduce the number of points in the polyline by removing redundant elements using Douglas–Peucker algorithm, so that result stays within <a href="sdk-for-flutter-explore-index">com.here.sdk.core.PolylineSimplifier.Options</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-379495459%2FClasslikes%2F1617540583" anchor-label="PowerType" id="-379495459%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Power</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-379495459%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">PowerType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">PowerType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Represents the type of electrical power. <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2005013819%2FClasslikes%2F1617540583" anchor-label="Rectangle2D" id="2005013819%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span><span>Rectangle2D</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2005013819%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">Rectangle2D</a></div><div class="brief "><p class="paragraph">Represents a 2D rectangle defined by the origin and size.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2078316263%2FClasslikes%2F1617540583" anchor-label="RouteType" id="-2078316263%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Route</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2078316263%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">RouteType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">RouteType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Indicates the level of significance of a route in a range from 1 to 6. A value of 1 stands for the most major route and 6 the most minor. The route type indicates that the road's name is actually a route number and in many countries is displayed in a shield symbol (e.g., Interstate and State routes in the U.S.). See https://developer.here.com/documentation/here-map-content-schema/dev_guide/topics_schema/streetname.routetype.html</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1334554898%2FClasslikes%2F1617540583" anchor-label="SDKLibraryLoader" id="1334554898%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>SDKLibrary</span><wbr></wbr><span><span>Loader</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1334554898%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">SDKLibraryLoader</a></div><div class="brief ">Loads HERE SDK native libraries.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="593318067%2FClasslikes%2F1617540583" anchor-label="Size2D" id="593318067%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span><span>Size2D</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="593318067%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">Size2D</a></div><div class="brief "><p class="paragraph">Represents the size of a 2D structure.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="729685725%2FClasslikes%2F1617540583" anchor-label="TimeRule" id="729685725%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Time</span><wbr></wbr><span><span>Rule</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="729685725%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">TimeRule</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a></div><div class="brief "><p class="paragraph">Used to indicate a time period of one or more intervals in <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/concepts/time-domain.html">GDF</a> specification. For example: -*(M3f21h2){M9}(M11f12h2){-M9}+(h15){h2}(h20){h2}, which represents: March 2nd Sunday 02h:00m for 9 months ONLY DURING November 1st Sunday 02h:00m from 9 months ago BUT NOT from 15:00 to 17:00 OR 20:00 to 22:00</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-209314074%2FClasslikes%2F1617540583" anchor-label="TransportProfile" id="-209314074%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Transport</span><wbr></wbr><span><span>Profile</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-209314074%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index"><strike>TransportProfile</strike></a></div><div class="brief "><p class="paragraph">Contains values of transport profile. This is a BETA feature and thus there can be bugs and unexpected behavior.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1831414643%2FClasslikes%2F1617540583" anchor-label="UnitSystem" id="1831414643%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Unit</span><wbr></wbr><span><span>System</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1831414643%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">UnitSystem</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">UnitSystem</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Represents the available unit systems(imperial/metric).</p></div></div></div>
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
`}</HTMLBlock>
