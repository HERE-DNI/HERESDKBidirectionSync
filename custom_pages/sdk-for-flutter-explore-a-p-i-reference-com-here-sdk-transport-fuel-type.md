---
title: "FuelType"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-fuel-type"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>FuelType</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.transport/FuelType///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.transport</a><span class="delimiter">/</span><span class="current">FuelType</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Fuel</span><wbr></wbr><span><span>Type</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="index.html">FuelType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="index.html">FuelType</a><span class="token operator">&gt; </span></div><p class="paragraph">Defines possible fuel types provided by a fuel station.</p><p class="paragraph"><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button><button class="section-tab" data-togglable="ENTRY">Entries</button></div>
    <div class="tabs-section-body">
      <div data-togglable="ENTRY">
        <h2 class="">Entries</h2>
        <div class="table"><a data-name="-358939999%2FClasslikes%2F1617540583" anchor-label="DIESEL" id="-358939999%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-d-i-e-s-e-l/index.html">DIESEL</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-358939999%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-d-i-e-s-e-l/index.html">DIESEL</a></div></div><div class="brief "><p class="paragraph">Diesel fuel type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="681166788%2FClasslikes%2F1617540583" anchor-label="LPG" id="681166788%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-l-p-g/index.html">LPG</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="681166788%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-l-p-g/index.html">LPG</a></div></div><div class="brief "><p class="paragraph">Liquified petroleum gas fuel type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2013334040%2FClasslikes%2F1617540583" anchor-label="BIO_DIESEL" id="2013334040%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-b-i-o_-d-i-e-s-e-l/index.html">BIO_DIESEL</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2013334040%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-b-i-o_-d-i-e-s-e-l/index.html">BIO_DIESEL</a></div></div><div class="brief "><p class="paragraph">Bio-Diesel fuel type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1237204989%2FClasslikes%2F1617540583" anchor-label="CNG" id="1237204989%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-c-n-g/index.html">CNG</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1237204989%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-c-n-g/index.html">CNG</a></div></div><div class="brief "><p class="paragraph">Compressed natural gas fuel type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1969932308%2FClasslikes%2F1617540583" anchor-label="DIESEL_WITH_ADDITIVES" id="1969932308%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-d-i-e-s-e-l_-w-i-t-h_-a-d-d-i-t-i-v-e-s/index.html">DIESEL_WITH_ADDITIVES</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1969932308%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-d-i-e-s-e-l_-w-i-t-h_-a-d-d-i-t-i-v-e-s/index.html">DIESEL_WITH_ADDITIVES</a></div></div><div class="brief "><p class="paragraph">Diesel with additives fuel type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1267229211%2FClasslikes%2F1617540583" anchor-label="E10" id="-1267229211%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-e10/index.html">E10</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1267229211%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-e10/index.html">E10</a></div></div><div class="brief "><p class="paragraph">10% Ethanol and 90% Gasoline fuel type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1559615036%2FClasslikes%2F1617540583" anchor-label="E20" id="-1559615036%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-e20/index.html">E20</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1559615036%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-e20/index.html">E20</a></div></div><div class="brief "><p class="paragraph">20% Ethanol and 80% Gasoline fuel type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2042256963%2FClasslikes%2F1617540583" anchor-label="E85" id="2042256963%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-e85/index.html">E85</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2042256963%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-e85/index.html">E85</a></div></div><div class="brief "><p class="paragraph">85% Ethanol and 15% Gasoline fuel type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="113001924%2FClasslikes%2F1617540583" anchor-label="ETHANOL" id="113001924%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-e-t-h-a-n-o-l/index.html">ETHANOL</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="113001924%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-e-t-h-a-n-o-l/index.html">ETHANOL</a></div></div><div class="brief "><p class="paragraph">Ethanol fuel type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1999403665%2FClasslikes%2F1617540583" anchor-label="ETHANOL_WITH_ADDITIVES" id="1999403665%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-e-t-h-a-n-o-l_-w-i-t-h_-a-d-d-i-t-i-v-e-s/index.html">ETHANOL_WITH_ADDITIVES</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1999403665%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-e-t-h-a-n-o-l_-w-i-t-h_-a-d-d-i-t-i-v-e-s/index.html">ETHANOL_WITH_ADDITIVES</a></div></div><div class="brief "><p class="paragraph">Ethanol with additives fuel type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1491770289%2FClasslikes%2F1617540583" anchor-label="GASOLINE" id="1491770289%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-g-a-s-o-l-i-n-e/index.html">GASOLINE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1491770289%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-g-a-s-o-l-i-n-e/index.html">GASOLINE</a></div></div><div class="brief "><p class="paragraph">Gasoline fuel type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1540662673%2FClasslikes%2F1617540583" anchor-label="GASOHOL_91" id="-1540662673%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-g-a-s-o-h-o-l_91/index.html">GASOHOL_91</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1540662673%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-g-a-s-o-h-o-l_91/index.html">GASOHOL_91</a></div></div><div class="brief "><p class="paragraph">Gasohol 91 fuel type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1885293427%2FClasslikes%2F1617540583" anchor-label="GASOHOL_95" id="1885293427%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-g-a-s-o-h-o-l_95/index.html">GASOHOL_95</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1885293427%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-g-a-s-o-h-o-l_95/index.html">GASOHOL_95</a></div></div><div class="brief "><p class="paragraph">Gasohol 95 fuel type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-915066622%2FClasslikes%2F1617540583" anchor-label="HVO" id="-915066622%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-h-v-o/index.html">HVO</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-915066622%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-h-v-o/index.html">HVO</a></div></div><div class="brief "><p class="paragraph">Hydrotreated vegetable oil fuel type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1744267801%2FClasslikes%2F1617540583" anchor-label="HYDROGEN" id="-1744267801%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-h-y-d-r-o-g-e-n/index.html">HYDROGEN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1744267801%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-h-y-d-r-o-g-e-n/index.html">HYDROGEN</a></div></div><div class="brief "><p class="paragraph">Hydrogen fuel type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1265938438%2FClasslikes%2F1617540583" anchor-label="LNG" id="1265938438%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-l-n-g/index.html">LNG</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1265938438%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-l-n-g/index.html">LNG</a></div></div><div class="brief "><p class="paragraph">Liquefied natural gas fuel type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1741728298%2FClasslikes%2F1617540583" anchor-label="MIDGRADE" id="-1741728298%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-m-i-d-g-r-a-d-e/index.html">MIDGRADE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1741728298%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-m-i-d-g-r-a-d-e/index.html">MIDGRADE</a></div></div><div class="brief "><p class="paragraph">Midgrade fuel type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="647629112%2FClasslikes%2F1617540583" anchor-label="PREMIUM" id="647629112%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-p-r-e-m-i-u-m/index.html">PREMIUM</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="647629112%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-p-r-e-m-i-u-m/index.html">PREMIUM</a></div></div><div class="brief "><p class="paragraph">Premium fuel type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1405673629%2FClasslikes%2F1617540583" anchor-label="PREMIUM_WITH_ADDITIVES" id="1405673629%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-p-r-e-m-i-u-m_-w-i-t-h_-a-d-d-i-t-i-v-e-s/index.html">PREMIUM_WITH_ADDITIVES</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1405673629%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-p-r-e-m-i-u-m_-w-i-t-h_-a-d-d-i-t-i-v-e-s/index.html">PREMIUM_WITH_ADDITIVES</a></div></div><div class="brief "><p class="paragraph">Premium with additives fuel type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1813538883%2FClasslikes%2F1617540583" anchor-label="REGULAR" id="-1813538883%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-r-e-g-u-l-a-r/index.html">REGULAR</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1813538883%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-r-e-g-u-l-a-r/index.html">REGULAR</a></div></div><div class="brief "><p class="paragraph">Regular fuel type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="481679224%2FClasslikes%2F1617540583" anchor-label="REGULAR_WITH_ADDITIVES" id="481679224%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-r-e-g-u-l-a-r_-w-i-t-h_-a-d-d-i-t-i-v-e-s/index.html">REGULAR_WITH_ADDITIVES</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="481679224%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-r-e-g-u-l-a-r_-w-i-t-h_-a-d-d-i-t-i-v-e-s/index.html">REGULAR_WITH_ADDITIVES</a></div></div><div class="brief "><p class="paragraph">Regular with additives fuel type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1727990631%2FClasslikes%2F1617540583" anchor-label="OCTANE_87" id="1727990631%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-o-c-t-a-n-e_87/index.html">OCTANE_87</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1727990631%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-o-c-t-a-n-e_87/index.html">OCTANE_87</a></div></div><div class="brief "><p class="paragraph">Octane 87 fuel type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1293485033%2FClasslikes%2F1617540583" anchor-label="OCTANE_89" id="1293485033%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-o-c-t-a-n-e_89/index.html">OCTANE_89</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1293485033%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-o-c-t-a-n-e_89/index.html">OCTANE_89</a></div></div><div class="brief "><p class="paragraph">Octane 89 fuel type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="808890751%2FClasslikes%2F1617540583" anchor-label="OCTANE_90" id="808890751%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-o-c-t-a-n-e_90/index.html">OCTANE_90</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="808890751%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-o-c-t-a-n-e_90/index.html">OCTANE_90</a></div></div><div class="brief "><p class="paragraph">Octane 90 fuel type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1555845696%2FClasslikes%2F1617540583" anchor-label="OCTANE_91" id="-1555845696%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-o-c-t-a-n-e_91/index.html">OCTANE_91</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1555845696%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-o-c-t-a-n-e_91/index.html">OCTANE_91</a></div></div><div class="brief "><p class="paragraph">Octane 91 fuel type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="374385153%2FClasslikes%2F1617540583" anchor-label="OCTANE_92" id="374385153%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-o-c-t-a-n-e_92/index.html">OCTANE_92</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="374385153%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-o-c-t-a-n-e_92/index.html">OCTANE_92</a></div></div><div class="brief "><p class="paragraph">Octane 92 fuel type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1990351294%2FClasslikes%2F1617540583" anchor-label="OCTANE_93" id="-1990351294%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-o-c-t-a-n-e_93/index.html">OCTANE_93</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1990351294%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-o-c-t-a-n-e_93/index.html">OCTANE_93</a></div></div><div class="brief "><p class="paragraph">Octane 93 fuel type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1870110404%2FClasslikes%2F1617540583" anchor-label="OCTANE_95" id="1870110404%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-o-c-t-a-n-e_95/index.html">OCTANE_95</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1870110404%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-o-c-t-a-n-e_95/index.html">OCTANE_95</a></div></div><div class="brief "><p class="paragraph">Octane 95 fuel type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-929131641%2FClasslikes%2F1617540583" anchor-label="OCTANE_98" id="-929131641%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-o-c-t-a-n-e_98/index.html">OCTANE_98</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-929131641%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-o-c-t-a-n-e_98/index.html">OCTANE_98</a></div></div><div class="brief "><p class="paragraph">Octane 98 fuel type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="623367985%2FClasslikes%2F1617540583" anchor-label="OCTANE_100" id="623367985%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-o-c-t-a-n-e_100/index.html">OCTANE_100</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="623367985%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-o-c-t-a-n-e_100/index.html">OCTANE_100</a></div></div><div class="brief "><p class="paragraph">Octane 100 fuel type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="443378529%2FProperties%2F1617540583" anchor-label="entries" id="443378529%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="entries.html"><span><span>entries</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="443378529%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="entries.html">entries</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html">EnumEntries</a><span class="token operator">&lt;</span><a href="index.html">FuelType</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Returns a representation of an immutable list of all enum entries, in the order they're declared.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1670387040%2FProperties%2F1617540583" anchor-label="value" id="-1670387040%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="value.html"><span><span>value</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1670387040%2FProperties%2F1617540583"></span>
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
        <div class="table"><a data-name="1154332635%2FFunctions%2F1617540583" anchor-label="valueOf" id="1154332635%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="value-of.html"><span>value</span><wbr></wbr><span><span>Of</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1154332635%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><a href="value-of.html"><span class="token function">valueOf</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">value<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">FuelType</a></div><div class="brief "><p class="paragraph">Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1323864103%2FFunctions%2F1617540583" anchor-label="values" id="1323864103%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="values.html"><span><span>values</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1323864103%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><a href="values.html"><span class="token function">values</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="token operator">&lt;</span><a href="index.html">FuelType</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Returns an array containing the constants of this enum type, in the order they're declared.</p></div></div></div>
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
