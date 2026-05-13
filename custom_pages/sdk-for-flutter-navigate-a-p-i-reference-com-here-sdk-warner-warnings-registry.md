---
title: "WarningsRegistry"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-warner-warnings-registry"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>WarningsRegistry</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.warner/WarningsRegistry///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.warner</a><span class="delimiter">/</span><span class="current">WarningsRegistry</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Warnings</span><wbr></wbr><span><span>Registry</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">WarningsRegistry</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a></div><p class="paragraph">A class that store warning metadata for different warning types. Aggregates individual collection for each warning category (safety cameras, truck restrictions, etc.). Provided by <code class="lang-kotlin">WarnerEngine</code> so callers can lookup detailed information about specific warnings.</p><p class="paragraph"><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-1114607928%2FClasslikes%2F1617540583" anchor-label="Companion" id="-1114607928%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1114607928%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">object </span><a href="-companion/index.html">Companion</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="266344763%2FFunctions%2F1617540583" anchor-label="getBorderCrossingWarning" id="266344763%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-border-crossing-warning.html"><span>get</span><wbr></wbr><span>Border</span><wbr></wbr><span>Crossing</span><wbr></wbr><span><span>Warning</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="266344763%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-border-crossing-warning.html"><span class="token function">getBorderCrossingWarning</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">warning<span class="token operator">: </span><a href="../-warning/index.html">Warning</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.navigation/-border-crossing-warning/index.html">BorderCrossingWarning</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Returns a border crossing warning corresponding to the given identifier.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-319475240%2FFunctions%2F1617540583" anchor-label="getCustomWarning" id="-319475240%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-custom-warning.html"><span>get</span><wbr></wbr><span>Custom</span><wbr></wbr><span><span>Warning</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-319475240%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-custom-warning.html"><span class="token function">getCustomWarning</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">warning<span class="token operator">: </span><a href="../-warning/index.html">Warning</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-custom-warning/index.html">CustomWarning</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Returns additional data associated with the given custom warning.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1378347802%2FFunctions%2F1617540583" anchor-label="getDangerZoneWarning" id="1378347802%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-danger-zone-warning.html"><span>get</span><wbr></wbr><span>Danger</span><wbr></wbr><span>Zone</span><wbr></wbr><span><span>Warning</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1378347802%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-danger-zone-warning.html"><span class="token function">getDangerZoneWarning</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">warning<span class="token operator">: </span><a href="../-warning/index.html">Warning</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.navigation/-danger-zone-warning/index.html">DangerZoneWarning</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Returns a danger zone warning corresponding to the given identifier.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1325962883%2FFunctions%2F1617540583" anchor-label="getEnvironmentalZoneWarning" id="1325962883%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-environmental-zone-warning.html"><span>get</span><wbr></wbr><span>Environmental</span><wbr></wbr><span>Zone</span><wbr></wbr><span><span>Warning</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1325962883%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-environmental-zone-warning.html"><span class="token function">getEnvironmentalZoneWarning</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">warning<span class="token operator">: </span><a href="../-warning/index.html">Warning</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.navigation/-environmental-zone-warning/index.html">EnvironmentalZoneWarning</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Returns environmental zone warning corresponding to the given identifier.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="187764863%2FFunctions%2F1617540583" anchor-label="getLaneDecreaseWarning" id="187764863%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-lane-decrease-warning.html"><span>get</span><wbr></wbr><span>Lane</span><wbr></wbr><span>Decrease</span><wbr></wbr><span><span>Warning</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="187764863%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-lane-decrease-warning.html"><span class="token function">getLaneDecreaseWarning</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">warning<span class="token operator">: </span><a href="../-warning/index.html">Warning</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-lane-decrease-warning/index.html">LaneDecreaseWarning</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Returns a lane decrease warning corresponding to the given identifier.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="452849258%2FFunctions%2F1617540583" anchor-label="getLowSpeedZoneWarning" id="452849258%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-low-speed-zone-warning.html"><span>get</span><wbr></wbr><span>Low</span><wbr></wbr><span>Speed</span><wbr></wbr><span>Zone</span><wbr></wbr><span><span>Warning</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="452849258%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-low-speed-zone-warning.html"><span class="token function">getLowSpeedZoneWarning</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">warning<span class="token operator">: </span><a href="../-warning/index.html">Warning</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.navigation/-low-speed-zone-warning/index.html">LowSpeedZoneWarning</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Returns a low speed zone warning corresponding to the given identifier.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-669189298%2FFunctions%2F1617540583" anchor-label="getRailwayCrossingWarning" id="-669189298%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-railway-crossing-warning.html"><span>get</span><wbr></wbr><span>Railway</span><wbr></wbr><span>Crossing</span><wbr></wbr><span><span>Warning</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-669189298%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-railway-crossing-warning.html"><span class="token function">getRailwayCrossingWarning</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">warning<span class="token operator">: </span><a href="../-warning/index.html">Warning</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.navigation/-railway-crossing-warning/index.html">RailwayCrossingWarning</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Returns a railway crossing warning corresponding to the given identifier.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="43753762%2FFunctions%2F1617540583" anchor-label="getRealisticViewWarning" id="43753762%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-realistic-view-warning.html"><span>get</span><wbr></wbr><span>Realistic</span><wbr></wbr><span>View</span><wbr></wbr><span><span>Warning</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="43753762%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-realistic-view-warning.html"><span class="token function">getRealisticViewWarning</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">warning<span class="token operator">: </span><a href="../-warning/index.html">Warning</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.navigation/-realistic-view-warning/index.html">RealisticViewWarning</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Returns a realistic-view warning corresponding to the given identifier.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="862767436%2FFunctions%2F1617540583" anchor-label="getRoadSignWarning" id="862767436%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-road-sign-warning.html"><span>get</span><wbr></wbr><span>Road</span><wbr></wbr><span>Sign</span><wbr></wbr><span><span>Warning</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="862767436%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-road-sign-warning.html"><span class="token function">getRoadSignWarning</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">warning<span class="token operator">: </span><a href="../-warning/index.html">Warning</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.navigation/-road-sign-warning/index.html">RoadSignWarning</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Returns a road-sign warning corresponding to the given identifier.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="895820402%2FFunctions%2F1617540583" anchor-label="getSafetyCameraWarning" id="895820402%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-safety-camera-warning.html"><span>get</span><wbr></wbr><span>Safety</span><wbr></wbr><span>Camera</span><wbr></wbr><span><span>Warning</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="895820402%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-safety-camera-warning.html"><span class="token function">getSafetyCameraWarning</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">warning<span class="token operator">: </span><a href="../-warning/index.html">Warning</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.navigation/-safety-camera-warning/index.html">SafetyCameraWarning</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Returns a safety-camera warning corresponding to the given identifier.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-319602775%2FFunctions%2F1617540583" anchor-label="getSchoolZoneWarning" id="-319602775%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-school-zone-warning.html"><span>get</span><wbr></wbr><span>School</span><wbr></wbr><span>Zone</span><wbr></wbr><span><span>Warning</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-319602775%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-school-zone-warning.html"><span class="token function">getSchoolZoneWarning</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">warning<span class="token operator">: </span><a href="../-warning/index.html">Warning</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.navigation/-school-zone-warning/index.html">SchoolZoneWarning</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Returns a school zone warning corresponding to the given identifier.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1939172972%2FFunctions%2F1617540583" anchor-label="getTollStopWarning" id="1939172972%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-toll-stop-warning.html"><span>get</span><wbr></wbr><span>Toll</span><wbr></wbr><span>Stop</span><wbr></wbr><span><span>Warning</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1939172972%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-toll-stop-warning.html"><span class="token function">getTollStopWarning</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">warning<span class="token operator">: </span><a href="../-warning/index.html">Warning</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.navigation/-toll-stop/index.html">TollStop</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Returns a toll stop warning corresponding to the given identifier.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-171201458%2FFunctions%2F1617540583" anchor-label="getTrafficMergeWarning" id="-171201458%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-traffic-merge-warning.html"><span>get</span><wbr></wbr><span>Traffic</span><wbr></wbr><span>Merge</span><wbr></wbr><span><span>Warning</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-171201458%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-traffic-merge-warning.html"><span class="token function">getTrafficMergeWarning</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">warning<span class="token operator">: </span><a href="../-warning/index.html">Warning</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.navigation/-traffic-merge-warning/index.html">TrafficMergeWarning</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Returns a traffic merge warning corresponding to the given identifier.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1832609884%2FFunctions%2F1617540583" anchor-label="getTruckRestrictionWarning" id="1832609884%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-truck-restriction-warning.html"><span>get</span><wbr></wbr><span>Truck</span><wbr></wbr><span>Restriction</span><wbr></wbr><span><span>Warning</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1832609884%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-truck-restriction-warning.html"><span class="token function">getTruckRestrictionWarning</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">warning<span class="token operator">: </span><a href="../-warning/index.html">Warning</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.navigation/-truck-restriction-warning/index.html">TruckRestrictionWarning</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Returns a truck restrictions warning corresponding to the given identifier.</p></div></div></div>
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
