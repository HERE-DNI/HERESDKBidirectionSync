---
title: "OfflineSearchEngine"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-search-offline-search-engine"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>OfflineSearchEngine</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.search/OfflineSearchEngine///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.search</a><span class="delimiter">/</span><span class="current">OfflineSearchEngine</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Offline</span><wbr></wbr><span>Search</span><wbr></wbr><span><span>Engine</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">OfflineSearchEngine</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a>, <a href="../-search-interface/index.html">SearchInterface</a></div><p class="paragraph">The OfflineSearchEngine works without internet and unlocks the search and geocoding capabilities of HERE services to provide developers with unmatched flexibility to create differentiating location-enabled applications.</p><p class="paragraph">It provides the same interfaces as the SearchEngine, but the results may slightly differ as the results are taken from already downloaded map data instead of initiating a new request to a HERE backend service. This way the data may be, for example, older compared to the data you may receive when using the SearchEngine. On the other hand, this class provides results faster as no online connection is necessary.</p><p class="paragraph">In comparison to the SearchEngine, there are a few limitations:</p><ul><li><p class="paragraph">The IDs of POIs are different and may differ among different map versions.</p></li><li><p class="paragraph">The implementation is different and the resources are limited, so the results can differ.</p></li><li><p class="paragraph">OfflineSearchEngine sometimes doesn't return the requested number of results.</p></li></ul><p class="paragraph">Note: You can search only within persistent map data (downloaded via MapDownloader) or existing cached data. However, cached data may be incomplete, which can result in searches returning partial or incomplete information. Therefore, it is recommended to use persistent map data. Make sure that at least <a href="../../com.here.sdk.core.engine/-layer-configuration/-feature/-o-f-f-l-i-n-e_-s-e-a-r-c-h/index.html">com.here.sdk.core.engine.LayerConfiguration.Feature.OFFLINE_SEARCH</a> is enabled. For EV rich attributes also enable <a href="../../com.here.sdk.core.engine/-layer-configuration/-feature/-e-v/index.html">com.here.sdk.core.engine.LayerConfiguration.Feature.EV</a>, for truck rich attributes also enable <a href="../../com.here.sdk.core.engine/-layer-configuration/-feature/-t-r-u-c-k_-s-e-r-v-i-c-e_-a-t-t-r-i-b-u-t-e-s/index.html">com.here.sdk.core.engine.LayerConfiguration.Feature.TRUCK_SERVICE_ATTRIBUTES</a>, for fuel station rich attributes also enable <a href="../../com.here.sdk.core.engine/-layer-configuration/-feature/-f-u-e-l_-s-t-a-t-i-o-n_-a-t-t-r-i-b-u-t-e-s/index.html">com.here.sdk.core.engine.LayerConfiguration.Feature.FUEL_STATION_ATTRIBUTES</a> in <a href="../../com.here.sdk.core.engine/-s-d-k-options/layer-configuration.html">com.here.sdk.core.engine.SDKOptions.layerConfiguration</a>.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="-1825140309%2FConstructors%2F1617540583" anchor-label="OfflineSearchEngine" id="-1825140309%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-offline-search-engine.html"><span>Offline</span><wbr></wbr><span>Search</span><wbr></wbr><span><span>Engine</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1825140309%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of this class.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">sdkEngine<span class="token operator">: </span><a href="../../com.here.sdk.core.engine/-s-d-k-native-engine/index.html">SDKNativeEngine</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of this class.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-2134182136%2FClasslikes%2F1617540583" anchor-label="Companion" id="-2134182136%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2134182136%2FClasslikes%2F1617540583"></span>
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
        <div class="table"><a data-name="-189130377%2FFunctions%2F1617540583" anchor-label="attach" id="-189130377%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="attach.html"><span><span>attach</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-189130377%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="attach.html"><span class="token function">attach</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">dataSource<span class="token operator">: </span><a href="../-my-places/index.html">MyPlaces</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-on-task-completed/index.html">OnTaskCompleted</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Attach data source into SearchEngine instance. Places from MyPlaces ranked the same way as places from default source. New data source replaces old one. Note: Only OfflineSearchEngine supports search over MyPlaces.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1549536648%2FFunctions%2F1617540583" anchor-label="search" id="1549536648%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="search.html"><span><span>search</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1549536648%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="search.html"><span class="token function">search</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">query<span class="token operator">: </span><a href="../-structured-query/index.html">StructuredQuery</a><span class="token punctuation">, </span></span><span class="parameter ">options<span class="token operator">: </span><a href="../-search-options/index.html">SearchOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-search-callback/index.html">SearchCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Performs an asynchronous request to search for places. The user submits a <a href="../-structured-query/index.html">com.here.sdk.search.StructuredQuery</a> that returns places adhering to the constraints provided in <a href="../-structured-query/index.html">com.here.sdk.search.StructuredQuery</a>. For example, when user wants results of type street for a text query <code class="lang-kotlin">Invalidenstraße</code> in <code class="lang-kotlin">Berlin</code>, it can be searched by preparing <a href="../-structured-query/index.html">com.here.sdk.search.StructuredQuery</a> providing <a href="../-structured-query/query.html">com.here.sdk.search.StructuredQuery.query</a> as <code class="lang-kotlin">Invalidenstraße</code>, <a href="../-structured-query/area-center.html">com.here.sdk.search.StructuredQuery.areaCenter</a>, <a href="../-structured-query/-address-elements/country.html">com.here.sdk.search.StructuredQuery.AddressElements.country</a> as <code class="lang-kotlin">Germany</code>, <a href="../-structured-query/-address-elements/city.html">com.here.sdk.search.StructuredQuery.AddressElements.city</a> as <code class="lang-kotlin">Berlin</code> and <a href="../-structured-query/-result-type/index.html">com.here.sdk.search.StructuredQuery.ResultType</a> as <code class="lang-kotlin">STREET</code>. The results will be presented only from the given geographical area.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1088598964%2FFunctions%2F1617540583" anchor-label="searchByAddress" id="-1088598964%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="search-by-address.html"><span>search</span><wbr></wbr><span>By</span><wbr></wbr><span><span>Address</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1088598964%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="search-by-address.html"><span class="token function">searchByAddress</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">query<span class="token operator">: </span><a href="../-address-query/index.html">AddressQuery</a><span class="token punctuation">, </span></span><span class="parameter ">options<span class="token operator">: </span><a href="../-search-options/index.html">SearchOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-search-callback/index.html">SearchCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Performs an asynchronous address query search for <a href="../-place/index.html">com.here.sdk.search.Place</a> instances. This is the same type of search as forward geocoding, except that more data is returned than just the geographic coordinates of a given address. Note that an address can belong to more than one <a href="../-place/index.html">com.here.sdk.search.Place</a> result, although all found places will share the same geographic coordinates. The returned places are sorted by relevance.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="351292678%2FFunctions%2F1617540583" anchor-label="searchByCategory" id="351292678%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="search-by-category.html"><span>search</span><wbr></wbr><span>By</span><wbr></wbr><span><span>Category</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="351292678%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="search-by-category.html"><span class="token function">searchByCategory</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">query<span class="token operator">: </span><a href="../-category-query/index.html">CategoryQuery</a><span class="token punctuation">, </span></span><span class="parameter ">options<span class="token operator">: </span><a href="../-search-options/index.html">SearchOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-search-callback/index.html">SearchCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Performs an asynchronous category search for <a href="../-place/index.html">com.here.sdk.search.Place</a> instances. A list containing at least one <a href="../-place-category/index.html">com.here.sdk.search.PlaceCategory</a> must be provided as part of the com.here.sdk.search.SearchInterface.searchByCategory.query.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1709770098%2FFunctions%2F1617540583" anchor-label="searchByCoordinates" id="1709770098%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="search-by-coordinates.html"><span>search</span><wbr></wbr><span>By</span><wbr></wbr><span><span>Coordinates</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1709770098%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="search-by-coordinates.html"><span class="token function">searchByCoordinates</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">coordinates<span class="token operator">: </span><a href="../../com.here.sdk.core/-geo-coordinates/index.html">GeoCoordinates</a><span class="token punctuation">, </span></span><span class="parameter ">options<span class="token operator">: </span><a href="../-search-options/index.html">SearchOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-search-callback/index.html">SearchCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Performs an asynchronous search for <a href="../-place/index.html">com.here.sdk.search.Place</a> instances based on the given geographic coordinates. This is the same search type as reverse geocoding, except that more data is returned than just the <a href="../-address/index.html">com.here.sdk.search.Address</a> related to the given coordinates. Note that more than one <a href="../-place/index.html">com.here.sdk.search.Place</a> can be related to the given coordinates. The returned places are sorted by relevance.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-797272268%2FFunctions%2F1617540583" anchor-label="searchByPickedPlace" id="-797272268%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="search-by-picked-place.html"><span>search</span><wbr></wbr><span>By</span><wbr></wbr><span>Picked</span><wbr></wbr><span><span>Place</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-797272268%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="search-by-picked-place.html"><span class="token function">searchByPickedPlace</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">pickedPlace<span class="token operator">: </span><a href="../../com.here.sdk.core/-picked-place/index.html">PickedPlace</a><span class="token punctuation">, </span></span><span class="parameter ">languageCode<span class="token operator">: </span><a href="../../com.here.sdk.core/-language-code/index.html">LanguageCode</a><span class="token operator">?</span><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-place-id-search-callback/index.html">PlaceIdSearchCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Performs an asynchronous search for a <a href="../-place/index.html">com.here.sdk.search.Place</a> based on the content found in <a href="../../com.here.sdk.core/-picked-place/index.html">com.here.sdk.core.PickedPlace</a>. If <a href="../../com.here.sdk.core/-picked-place/index.html">com.here.sdk.core.PickedPlace</a> data is obtained from the offline map, it may happen that the newer version that is used by the online service represented by <code class="lang-kotlin">SearchEngine</code> no longer contains the related POI. In that case, <a href="../-search-error/-n-o_-r-e-s-u-l-t-s_-f-o-u-n-d/index.html">com.here.sdk.search.SearchError.NO_RESULTS_FOUND</a> error is reported. When that happens, you may try to obtain the POI from the offline map by calling <code class="lang-kotlin">OfflineSearchEngine.searchByPickedPlace</code>, only available for the Navigate license.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="89457631%2FFunctions%2F1617540583" anchor-label="searchByPlaceId" id="89457631%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="search-by-place-id.html"><span>search</span><wbr></wbr><span>By</span><wbr></wbr><span>Place</span><wbr></wbr><span><span>Id</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="89457631%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="search-by-place-id.html"><span class="token function">searchByPlaceId</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">query<span class="token operator">: </span><a href="../-place-id-query/index.html">PlaceIdQuery</a><span class="token punctuation">, </span></span><span class="parameter ">languageCode<span class="token operator">: </span><a href="../../com.here.sdk.core/-language-code/index.html">LanguageCode</a><span class="token operator">?</span><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-place-id-search-callback/index.html">PlaceIdSearchCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Performs an asynchronous search for a <a href="../-place/index.html">com.here.sdk.search.Place</a> based on its ID and <a href="../../com.here.sdk.core/-language-code/index.html">com.here.sdk.core.LanguageCode</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1738596520%2FFunctions%2F1617540583" anchor-label="searchByText" id="1738596520%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="search-by-text.html"><span>search</span><wbr></wbr><span>By</span><wbr></wbr><span><span>Text</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1738596520%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="search-by-text.html"><span class="token function">searchByText</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">query<span class="token operator">: </span><a href="../-text-query/index.html">TextQuery</a><span class="token punctuation">, </span></span><span class="parameter ">options<span class="token operator">: </span><a href="../-search-options/index.html">SearchOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-search-callback/index.html">SearchCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Performs an asynchronous text query search for <a href="../-place/index.html">com.here.sdk.search.Place</a> instances within a given <a href="../-text-query/-area/index.html">com.here.sdk.search.TextQuery.Area</a>. The returned places are sorted by relevance.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-797276744%2FFunctions%2F1617540583" anchor-label="suggest" id="-797276744%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="suggest.html"><span><span>suggest</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-797276744%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="suggest.html"><span class="token function">suggest</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">query<span class="token operator">: </span><a href="../-structured-query/index.html">StructuredQuery</a><span class="token punctuation">, </span></span><span class="parameter ">options<span class="token operator">: </span><a href="../-search-options/index.html">SearchOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-suggest-callback/index.html">SuggestCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Performs an asynchronous request to suggest places for a <a href="../-structured-query/index.html">com.here.sdk.search.StructuredQuery</a> built with address elements and returns candidate suggestions sorted by relevance. For example, when user wants suggestions of type street for a text query <code class="lang-kotlin">Invalidenstraße</code> in <code class="lang-kotlin">Berlin</code>, it can be searched by preparing <a href="../-structured-query/index.html">com.here.sdk.search.StructuredQuery</a> providing <a href="../-structured-query/query.html">com.here.sdk.search.StructuredQuery.query</a> as <code class="lang-kotlin">Invalidenstraße</code>, <a href="../-structured-query/area-center.html">com.here.sdk.search.StructuredQuery.areaCenter</a>, <a href="../-structured-query/-address-elements/country.html">com.here.sdk.search.StructuredQuery.AddressElements.country</a> as <code class="lang-kotlin">Germany</code>, <a href="../-structured-query/-address-elements/city.html">com.here.sdk.search.StructuredQuery.AddressElements.city</a> as <code class="lang-kotlin">Berlin</code> and <a href="../-structured-query/-result-type/index.html">com.here.sdk.search.StructuredQuery.ResultType</a> as <code class="lang-kotlin">STREET</code>. The suggestions will be presented only from the given geographical area.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="768611992%2FFunctions%2F1617540583" anchor-label="suggestByText" id="768611992%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="suggest-by-text.html"><span>suggest</span><wbr></wbr><span>By</span><wbr></wbr><span><span>Text</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="768611992%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="suggest-by-text.html"><span class="token function">suggestByText</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">query<span class="token operator">: </span><a href="../-text-query/index.html">TextQuery</a><span class="token punctuation">, </span></span><span class="parameter ">options<span class="token operator">: </span><a href="../-search-options/index.html">SearchOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-suggest-callback/index.html">SuggestCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Performs an asynchronous request to suggest places for text queries and returns suggestions sorted by relevance.</p></div></div></div>
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
