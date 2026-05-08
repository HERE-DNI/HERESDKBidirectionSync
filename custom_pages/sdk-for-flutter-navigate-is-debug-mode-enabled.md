---
title: "isDebugModeEnabled"
slug: "sdk-for-flutter-navigate-is-debug-mode-enabled"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- is-debug-mode-enabled.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>isDebugModeEnabled</title>
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
<div class="main-content" data-page-type="member" id="content" pageIds="API Reference::com.here.sdk.navigation/VisualNavigator/isDebugModeEnabled/#/PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.navigation</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">VisualNavigator</a><span class="delimiter">/</span><span class="current">isDebugModeEnabled</span></div>
  <div class="cover ">
    <h1 class="cover"><span>is</span><wbr></wbr><span>Debug</span><wbr></wbr><span>Mode</span><wbr></wbr><span><span>Enabled</span></span></h1>
  </div>
  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-is-debug-mode-enabled">isDebugModeEnabled</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><p class="paragraph">When enabled, it shows useful information for debugging purposes.</p><ul><li><p class="paragraph">A semi-transparent location marker indicating the map-matched location.</p></li><li><p class="paragraph">A gray, semi-transparent location marker indicating the raw (or original) input location.</p></li><li><p class="paragraph">A red polyline indicating the most probable path.</p></li><li><p class="paragraph">A SVG overlay, on the middle-left of the screen, showing the following:</p></li><li><p class="paragraph">IN - Input location: coordinates \[bearing\] \[speed] \[accuracy\]</p></li><li><p class="paragraph">RM - Route-matched location: coordinates bearing (distance-to-raw-location)</p></li><li><p class="paragraph">MM - Map-Matched location: coordinates bearing (distance-to-raw-location)</p></li><li><p class="paragraph">RM-MM - distance-between-route-and-map-matched-locations</p></li><li><p class="paragraph">RP - Route progress: remaining-duration remaining-distance</p></li><li><p class="paragraph">SP - Section progress: section-index/sections-count remaining-duration remaining-distance</p></li><li><p class="paragraph">MP - Maneuver progress: maneuver-index remaining-duration remaining-distance</p></li><li><p class="paragraph">CPU - CPU usage: cpu-usage current-date-time</p></li><li><p class="paragraph">MS - Milestone status: section-index MISSED|REACHED when</p></li><li><p class="paragraph">RD - Route deviation: last-traveled-section-index last-traveled-section-distance when</p></li><li><p class="paragraph">FPS - Frames per second: frames-per-second</p></li></ul><p class="paragraph">Fields between brackets (\[\]'s) are omitted if not available.</p><p class="paragraph">Example:</p><pre>
IN: 53.96880,14.77903 167° 8m/s
RM: 53.96880,14.77903 167° (0.0m)
MM: 53.96879,14.77903 167° (0.5m)
RM-MM: 0.5m
RP: 49h0m3s 4302km
SP: 0/16 1h2m20s 58km
MP: 1 5s 25m
CPU: 7% 2024-01-01 13:21:59
MS: 1 REACHED 12:34:22
RD: 2 345m 11:13:55
FPS: 30.0
</pre><p class="paragraph"><strong>Note:</strong> This API should be used for debugging purposes only.</p></div></div>
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
