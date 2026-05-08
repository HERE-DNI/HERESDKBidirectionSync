---
title: "setCustomOption"
slug: "sdk-for-flutter-explore-set-custom-option"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- set-custom-option.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>setCustomOption</title>
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
<div class="main-content" data-page-type="member" id="content" pageIds="API Reference::com.here.sdk.search/SearchEngine/setCustomOption/#kotlin.String#kotlin.String/PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.search</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">SearchEngine</a><span class="delimiter">/</span><span class="current">setCustomOption</span></div>
  <div class="cover ">
    <h1 class="cover"><span>set</span><wbr></wbr><span>Custom</span><wbr></wbr><span><span>Option</span></span></h1>
  </div>
  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-custom-option"><span class="token function">setCustomOption</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">name<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token punctuation">, </span></span><span class="parameter ">value<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">SearchError</a><span class="token operator">?</span></div><p class="paragraph">Sets a custom option for search backend queries. This allows more control over the behavior of the search algorithm. Name has the format <endpoint_name>.<option_name>, for example &quot;discover.show&quot;. Values can be combined for the same name by using a comma, for example &quot;truck,fuel&quot;. The custom option is applied only for the endpoint that is specified as prefix in <code class="lang-kotlin">name</code>. Some of the supported name/value options are:</p><ul><li><p class="paragraph">name = &quot;revgeocode.with&quot;, value = &quot;unnamedStreets&quot; enables the retrieval of access points on unnamed streets.</p></li><li><p class="paragraph">name = &quot;lookup.show&quot; or &quot;discover.show&quot; or &quot;autosuggest.show&quot; or &quot;browse.show&quot;, value = &quot;truck&quot; enables retreival of truck amenities. <strong>Note:</strong> Only participants of the closed-alpha group can get access from HERE to use this feature, otherwise, a <a href="sdk-for-flutter-explore-index">com.here.sdk.search.SearchError.FORBIDDEN</a> will be propagated in callbacks.</p></li><li><p class="paragraph">name = &quot;lookup.show&quot; or &quot;discover.show&quot; or &quot;autosuggest.show&quot; or &quot;browse.show&quot;, value = &quot;fuel&quot; enables retreival of fuel station details. <strong>Note:</strong> Only participants of the closed-alpha group can get access from HERE to use this feature, otherwise, a <a href="sdk-for-flutter-explore-index">com.here.sdk.search.SearchError.FORBIDDEN</a> will be propagated in callbacks.</p></li><li><p class="paragraph">name = &quot;lookup.show&quot; or &quot;discover.show&quot; or &quot;browse.show&quot;, value = &quot;ev&quot; enables retreival of EV charging station details.</p></li><li><p class="paragraph">name = &quot;lookup.show&quot; or &quot;discover.show&quot; or &quot;browse.show&quot;, value = &quot;eMobilityServiceProviders&quot; enables retreival of e-Mobility Service Providers details.</p></li><li><p class="paragraph">name = &quot;lookup.show&quot; or &quot;discover.show&quot; or &quot;browse.show&quot;, value = &quot;tripadvisor&quot; adds images, ratings, and editorials from Tripadvisor (TM). <strong>Note:</strong> Only clients with a license with TripAdvisor for rich content will actually get it. If this licence is missing, TripAdvisor rich content will be missing, with no error reported. This content is only added to top 10 search results. If more results are returned, they will be missing rich TripAdvisor content.</p></li><li><p class="paragraph">name = &quot;lookup.datasets&quot; or &quot;discover.datasets&quot; or &quot;browse.datasets&quot; or &quot;autosuggest.datasets&quot;, value = <your_dataset_hrn> enables ingesting and searching of private POIs. <strong>Note:</strong> Only participants of the search customization can get access from HERE to use this feature, otherwise, a <a href="sdk-for-flutter-explore-index">com.here.sdk.search.SearchError.INVALID_CUSTOM_OPTION_FORMAT</a> will be propagated in callbacks.</p></li><li><p class="paragraph">name = &quot;discover.ranking&quot; or &quot;browse.ranking&quot;, value = &quot;excursionDistance&quot; enables balanced distribution of results for search in <code class="lang-kotlin">GeoCorridor</code>. Constraint: using this parameter when searching an area that is not a <code class="lang-kotlin">GeoCorridor</code> generates an error <a href="sdk-for-flutter-explore-index">com.here.sdk.search.SearchError.BAD_REQUEST</a>. <strong>Note:</strong> It is recommended to use <a href="sdk-for-flutter-explore-distributed-results">com.here.sdk.search.SearchOptions.distributedResults</a> instead. For a complete list of available endpoints, parameter names and their valid values, refer to <a href="https://www.here.com/docs/bundle/batch-api-developer-guide/page/topics/constructing-request.html">HERE Geocoding & Search API v7</a>. <strong>Note:</strong> It's easy to set a wrong option that makes queries invalid, so make sure you read and understand the backend documentation.</p></li></ul><span class="kdoc-tag"><h4 class="">Return</h4><p class="paragraph">Error in case when setting the option fails.</p></span><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>name</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Option name in the format <endpoint_name>.<option_name>, for example &quot;discover.show&quot;.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>value</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Option value.</p></div></div></div></div></div></div></div>
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
