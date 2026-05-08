---
title: "TextStyle"
slug: "sdk-for-flutter-explore--text-style"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- -text-style.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>TextStyle</title>
    <link href="../../../../images/logo-icon.svg" rel="icon" type="image/svg">
    <script>var pathToRoot = "../../../../";</script>
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
<script type="text/javascript" src="../../../../scripts/sourceset_dependencies.js" async="async"></script>
<link href="../../../../styles/style.css" rel="Stylesheet">
<link href="../../../../styles/main.css" rel="Stylesheet">
<link href="../../../../styles/prism.css" rel="Stylesheet">
<link href="../../../../styles/logo-styles.css" rel="Stylesheet">
<link href="../../../../styles/font-jb-sans-auto.css" rel="Stylesheet">
<link href="../../../../ui-kit/ui-kit.min.css" rel="Stylesheet">
<script type="text/javascript" src="../../../../scripts/clipboard.js" async="async"></script>
<script type="text/javascript" src="../../../../scripts/navigation-loader.js" async="async"></script>
<script type="text/javascript" src="../../../../scripts/platform-content-handler.js" async="async"></script>
<script type="text/javascript" src="../../../../scripts/main.js" defer="defer"></script>
<script type="text/javascript" src="../../../../scripts/prism.js" async="async"></script>
<script type="text/javascript" src="../../../../ui-kit/ui-kit.min.js" defer="defer"></script>
<script type="text/javascript" src="../../../../scripts/symbol-parameters-wrapper_deferred.js" defer="defer"></script>
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
<div class="main-content" data-page-type="member" id="content" pageIds="API Reference::com.here.sdk.mapview/MapMarker.TextStyle/TextStyle/#/PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.mapview</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">MapMarker</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">TextStyle</a><span class="delimiter">/</span><span class="current">TextStyle</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Text</span><wbr></wbr><span><span>Style</span></span></h1>
  </div>
  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="token punctuation">)</span></div><p class="paragraph">Creates a default set of styling options for the text of a <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapMarker</a> that consists of the following values:</p><ul><li><p class="paragraph">Text size: 18 pixels</p></li><li><p class="paragraph">Text color: opaque white</p></li><li><p class="paragraph">Text outline size: 0 pixels</p></li><li><p class="paragraph">Text outline color: opaque black</p></li><li><p class="paragraph">Text placement: <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapMarker.TextStyle.Placement.BOTTOM</a></p></li></ul><p class="paragraph">Once the resulting <code class="lang-kotlin">TextStyle</code> is applied to a <code class="lang-kotlin">MapMarker</code>, its text will be centered over its image. The font will be 18 pixels wide, colored opaque white and will have no visible outline.</p><hr><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">textSize<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token punctuation">, </span></span><span class="parameter ">textColor<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Color</a><span class="token punctuation">, </span></span><span class="parameter ">textOutlineSize<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token punctuation">, </span></span><span class="parameter ">textOutlineColor<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Color</a><span class="token punctuation">, </span></span><span class="parameter ">placements<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="sdk-for-flutter-explore-index">MapMarker.TextStyle.Placement</a><span class="token operator">&gt;</span></span></span><span class="token punctuation">)</span></div><p class="paragraph">Creates a set of styling options for the text of a <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapMarker</a>.</p><p class="paragraph">List of placements is used to specify allowed placement of text relative to the icon. When marker overlapping is allowed as set by <a href="sdk-for-flutter-explore-is-overlap-allowed">com.here.sdk.mapview.MapMarker.isOverlapAllowed</a>, only first placement element is considered. Otherwise the placement value is chosen so that the text does not overlap with other <code class="lang-kotlin">MapMarker</code> instances.</p><p class="paragraph">Placement values are prioritized according to the order in which they appear in the list. Lists with duplicate entries as well as empty lists are not supported.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>text</span><wbr></wbr><span><span>Size</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The size of the text in pixels.     Only positive values are supported.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>text</span><wbr></wbr><span><span>Color</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The text color.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>text</span><wbr></wbr><span>Outline</span><wbr></wbr><span><span>Size</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The size of the text outline in pixels.     Only non-negative values are supported.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>text</span><wbr></wbr><span>Outline</span><wbr></wbr><span><span>Color</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The color of the text outline.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>placements</span></span></u></div></span></div><div><div class="title"><p class="paragraph">List of allowed placements of the text relative to the icon of a <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapMarker</a>.</p></div></div></div></div></div><h4 class="">Throws</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><a href="sdk-for-flutter-explore-index"><span>MapMarker.</span><wbr></wbr><span>TextStyle.</span><wbr></wbr><span>Instantiation</span><wbr></wbr><span><span>Exception</span></span></a></div></span></div><div><div class="title"><p class="paragraph">In case of invalid input parameters.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">textSize<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token punctuation">, </span></span><span class="parameter ">textColor<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Color</a><span class="token punctuation">, </span></span><span class="parameter ">textOutlineSize<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token punctuation">, </span></span><span class="parameter ">textOutlineColor<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Color</a><span class="token punctuation">, </span></span><span class="parameter ">placements<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="sdk-for-flutter-explore-index">MapMarker.TextStyle.Placement</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">fontName<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Creates a set of styling options for the text of a <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapMarker</a>.</p><p class="paragraph">Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.</p><p class="paragraph">List of placements is used to specify allowed placement of text relative to the icon. When marker overlapping is allowed as set by <a href="sdk-for-flutter-explore-is-overlap-allowed">com.here.sdk.mapview.MapMarker.isOverlapAllowed</a>, only first placement element is considered. Otherwise the placement value is chosen so that the text does not overlap with other <code class="lang-kotlin">MapMarker</code> instances.</p><p class="paragraph">Placement values are prioritized according to the order in which they appear in the list. Lists with duplicate entries as well as empty lists are not supported.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>text</span><wbr></wbr><span><span>Size</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The size of the text in pixels.     Only positive values are supported.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>text</span><wbr></wbr><span><span>Color</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The text color.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>text</span><wbr></wbr><span>Outline</span><wbr></wbr><span><span>Size</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The size of the text outline in pixels.     Only non-negative values are supported.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>text</span><wbr></wbr><span>Outline</span><wbr></wbr><span><span>Color</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The color of the text outline.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>placements</span></span></u></div></span></div><div><div class="title"><p class="paragraph">List of allowed placements of the text relative to the icon of a <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapMarker</a>.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>font</span><wbr></wbr><span><span>Name</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Font name, registered with <code class="lang-kotlin">AssetsManager.registerFont</code>.     If empty string is provided, a default font will be used.</p></div></div></div></div></div><h4 class="">Throws</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><a href="sdk-for-flutter-explore-index"><span>MapMarker.</span><wbr></wbr><span>TextStyle.</span><wbr></wbr><span>Instantiation</span><wbr></wbr><span><span>Exception</span></span></a></div></span></div><div><div class="title"><p class="paragraph">In case of invalid input parameters.</p></div></div></div></div></div></div></div>
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
