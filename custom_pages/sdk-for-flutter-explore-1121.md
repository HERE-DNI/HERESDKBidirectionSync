---
title: "MAP_CONTENT"
slug: "sdk-for-flutter-explore"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>MAP_CONTENT</title>
    <link href="../../../../../../images/logo-icon.svg" rel="icon" type="image/svg">
    <script>var pathToRoot = "../../../../../../";</script>
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
<script type="text/javascript" src="../../../../../../scripts/sourceset_dependencies.js" async="async"></script>
<link href="../../../../../../styles/style.css" rel="Stylesheet">
<link href="../../../../../../styles/main.css" rel="Stylesheet">
<link href="../../../../../../styles/prism.css" rel="Stylesheet">
<link href="../../../../../../styles/logo-styles.css" rel="Stylesheet">
<link href="../../../../../../styles/font-jb-sans-auto.css" rel="Stylesheet">
<link href="../../../../../../ui-kit/ui-kit.min.css" rel="Stylesheet">
<script type="text/javascript" src="../../../../../../scripts/clipboard.js" async="async"></script>
<script type="text/javascript" src="../../../../../../scripts/navigation-loader.js" async="async"></script>
<script type="text/javascript" src="../../../../../../scripts/platform-content-handler.js" async="async"></script>
<script type="text/javascript" src="../../../../../../scripts/main.js" defer="defer"></script>
<script type="text/javascript" src="../../../../../../scripts/prism.js" async="async"></script>
<script type="text/javascript" src="../../../../../../ui-kit/ui-kit.min.js" defer="defer"></script>
<script type="text/javascript" src="../../../../../../scripts/symbol-parameters-wrapper_deferred.js" defer="defer"></script>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.mapview/MapScene.MapPickFilter.ContentType.MAP_CONTENT///PointingToDeclaration/{&quot;org.jetbrains.dokka.links.EnumEntryDRIExtra&quot;:{&quot;key&quot;:&quot;org.jetbrains.dokka.links.EnumEntryDRIExtra&quot;}}/1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.mapview</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">MapScene</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">MapPickFilter</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">ContentType</a><span class="delimiter">/</span><span class="current">MAP_CONTENT</span></div>
  <div class="cover ">
    <h1 class="cover"><span>MAP_</span><wbr></wbr><span>CONTENT</span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">MAP_CONTENT</a></div></div><p class="paragraph">Pickable map content currently consists of:</p><ul><li><p class="paragraph">Embedded carto POI markers that by default are available on the map.</p></li><li><p class="paragraph">Traffic incidents that are visible when they are enabled using <a href="sdk-for-flutter-explore-enable-features">com.here.sdk.mapview.MapScene.enableFeatures</a> with <a href="sdk-for-flutter-explore-t-r-a-f-f-i-c-i-n-c-i-d-e-n-t-s">com.here.sdk.mapview.MapFeatures.TRAFFIC_INCIDENTS</a>.</p></li><li><p class="paragraph">Vehicle restrictions are only available for the Navigate license. Vehicle restrictions are enabled using <a href="sdk-for-flutter-explore-enable-features">com.here.sdk.mapview.MapScene.enableFeatures</a> with <code class="lang-kotlin">MapFeatures.VEHICLE_RESTRICTIONS</code>. Please note that the vehicle restriction line marking the affected street is pickable and not the restriction icon itself. Only visible POIs, traffic incidents and vehicle restrictions lines can be picked, i.e. only those categories that are not hidden and those that are not covered by any custom marker.</p></li></ul></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"></div>
    <div class="tabs-section-body"></div>
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
