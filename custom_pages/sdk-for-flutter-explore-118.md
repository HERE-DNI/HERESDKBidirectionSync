---
title: "Feature"
slug: "sdk-for-flutter-explore"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>Feature</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.core.engine/LayerConfiguration.Feature///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.core.engine</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">LayerConfiguration</a><span class="delimiter">/</span><span class="current">Feature</span></div>
  <div class="cover ">
    <h1 class="cover"><span><span>Feature</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">Feature</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">LayerConfiguration.Feature</a><span class="token operator">&gt; </span></div><p class="paragraph">Defines a list of possible map data features that can be enabled / disabled. See <a href="sdk-for-flutter-explore-layer-configuration">com.here.sdk.core.engine.SDKOptions.layerConfiguration</a></p><p class="paragraph">Following features are enabled by default:</p><ul><li><p class="paragraph"><a href="sdk-for-flutter-explore-index">com.here.sdk.core.engine.LayerConfiguration.Feature.DETAIL_RENDERING</a></p></li><li><p class="paragraph"><a href="sdk-for-flutter-explore-index">com.here.sdk.core.engine.LayerConfiguration.Feature.LANDMARKS_3D</a></p></li><li><p class="paragraph"><a href="sdk-for-flutter-explore-index">com.here.sdk.core.engine.LayerConfiguration.Feature.NAVIGATION</a></p></li><li><p class="paragraph"><a href="sdk-for-flutter-explore-index">com.here.sdk.core.engine.LayerConfiguration.Feature.OFFLINE_SEARCH</a></p></li><li><p class="paragraph"><a href="sdk-for-flutter-explore-index">com.here.sdk.core.engine.LayerConfiguration.Feature.OFFLINE_ROUTING</a></p></li><li><p class="paragraph"><a href="sdk-for-flutter-explore-index">com.here.sdk.core.engine.LayerConfiguration.Feature.RENDERING</a></p></li></ul><p class="paragraph">All other features are disabled, by default.</p><p class="paragraph">Each feature enables a set of OCM layer groups to be downloaded by <code class="lang-kotlin">sdk.maploader.MapDownloader</code>. Detailed description of each layer group available in the <a href="https://www.here.com/docs/bundle/optimized-client-map-developer-guide/page/README.html">HERE Optimized Client Map Developer Guide</a></p><p class="paragraph">Following features are enabled by default for implicit prefetch:</p><ul><li><p class="paragraph"><a href="sdk-for-flutter-explore-index">com.here.sdk.core.engine.LayerConfiguration.Feature.NAVIGATION</a></p></li></ul><p class="paragraph">Implicit prefetch downloads map content for implicit prefetch features within a view port currently showed by MapView. Explicit prefetching is done using <code class="lang-kotlin">sdk.prefetcher.RoutePrefetcher</code> and <code class="lang-kotlin">sdk.prefetcher.PolygonPrefetcher</code>.</p><p class="paragraph">Feature might have more than one layer group predefined to enable full experience. For example, <a href="sdk-for-flutter-explore-index">com.here.sdk.core.engine.LayerConfiguration.Feature.NAVIGATION</a> requires routing attributes, visual-friendly street names, maneuvers data and ability to interconnect those data sets.</p><p class="paragraph">The same map data is useful for different features, for example <a href="sdk-for-flutter-explore-index">com.here.sdk.core.engine.LayerConfiguration.Feature.RENDERING</a> uses Places data to present it on the MapView, while <a href="sdk-for-flutter-explore-index">com.here.sdk.core.engine.LayerConfiguration.Feature.OFFLINE_SEARCH</a> uses the same data to enable discoverability by name or category. Hence, features might have overlapping sets of enabled layer groups.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button><button class="section-tab" data-togglable="ENTRY">Entries</button></div>
    <div class="tabs-section-body">
      <div data-togglable="ENTRY">
        <h2 class="">Entries</h2>
        <div class="table"><a data-name="1277872048%2FClasslikes%2F1617540583" anchor-label="DETAIL_RENDERING" id="1277872048%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">DETAIL_RENDERING</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1277872048%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">DETAIL_RENDERING</a></div></div><div class="brief "><p class="paragraph">Additional rendering details like buildings. Only used for the MapView. When not set, the data will be excluded when downloading offline regions or prefetching areas that contain such data. However, during online usage such data may still be downloaded into the cache and shown. Increase of 11-16% is to be expected for map size, in case of enabling this feature.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1552699962%2FClasslikes%2F1617540583" anchor-label="NAVIGATION" id="-1552699962%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">NAVIGATION</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1552699962%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">NAVIGATION</a></div></div><div class="brief "><p class="paragraph">Map data that is used for map matching during navigation. When not set, navigation may not work properly when being used offline. Increase of 5-7% is to be expected for map size, but pay attention, that this feature is depended on other layer groups (e.g. routing), so, in total is takes about 21-29 % of map size.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="322365526%2FClasslikes%2F1617540583" anchor-label="OFFLINE_SEARCH" id="322365526%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">OFFLINE_SEARCH</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="322365526%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">OFFLINE_SEARCH</a></div></div><div class="brief "><p class="paragraph">Map data that is used to search. When not set, the OfflineSearchEngine may not work properly when being used offline.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1322732076%2FClasslikes%2F1617540583" anchor-label="OFFLINE_SEARCH_GLOBAL" id="-1322732076%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">OFFLINE_SEARCH_GLOBAL</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1322732076%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">OFFLINE_SEARCH_GLOBAL</a></div></div><div class="brief "><p class="paragraph">Map data used for global search indexing. This feature enables searches across broader geographic areas and improves both performance and accuracy by leveraging global search indices. By default this feature is disabled.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="854645728%2FClasslikes%2F1617540583" anchor-label="OFFLINE_ROUTING" id="854645728%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">OFFLINE_ROUTING</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="854645728%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">OFFLINE_ROUTING</a></div></div><div class="brief "><p class="paragraph">Map data that is used to calculate routes. When not set, the OfflineRoutingEngine may not work properly when being used offline.  Increase of 12-16.5% is to be expected for map size, but pay attention, that this feature is depended on other layer groups (e.g. navigation), so, in total is takes about 33-45 % of map size.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1474756062%2FClasslikes%2F1617540583" anchor-label="RENDERING" id="-1474756062%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">RENDERING</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1474756062%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">RENDERING</a></div></div><div class="brief "><p class="paragraph">A basic set of rendering features such as carto POIs. Increase of 16-22% is to be expected for map size, but pay attention, that this feature is depended on other layer groups (e.g. navigation), so, in total is takes about 21-29 % of map size.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1648712117%2FClasslikes%2F1617540583" anchor-label="TRUCK" id="1648712117%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">TRUCK</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1648712117%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">TRUCK</a></div></div><div class="brief "><p class="paragraph">Map data that is used to calculate truck routes. When not set, the <code class="lang-kotlin">OfflineRoutingEngine</code> may not work properly when being used to calculate truck routes. It is also used for map matching during truck navigation and for vehicle restriction visualization. When not set, truck navigation may not work properly when being used offline. Online truck navigation will still work when the device has an online connection. Increase of 0.7-1.1% is to be expected for map size, in case of enabling this feature. By default this feature is disabled.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-697464441%2FClasslikes%2F1617540583" anchor-label="LANDMARKS_3D" id="-697464441%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">LANDMARKS_3D</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-697464441%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">LANDMARKS_3D</a></div></div><div class="brief "><p class="paragraph">Map data that is used to render 3D landmarks. When not set, the data will be excluded when downloading offline regions or prefetching areas that contain such data. When the <code class="lang-kotlin">landmarks</code> <code class="lang-kotlin">MapFeature</code> is set to be visible for a <code class="lang-kotlin">MapScene</code>, 3D landmarks will still be loaded and visible during online usage. Increase of 2-3% is to be expected for map size, in case of enabling this feature.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1912409693%2FClasslikes%2F1617540583" anchor-label="EV" id="-1912409693%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">EV</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1912409693%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">EV</a></div></div><div class="brief "><p class="paragraph">Offline map data for <code class="lang-kotlin">EVChargingStation</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1274224717%2FClasslikes%2F1617540583" anchor-label="TRUCK_SERVICE_ATTRIBUTES" id="-1274224717%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">TRUCK_SERVICE_ATTRIBUTES</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1274224717%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">TRUCK_SERVICE_ATTRIBUTES</a></div></div><div class="brief "><p class="paragraph">Enables truck related attributes to be returned by Offline Search engine. Feature enables following OCM layer groups:</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="598282881%2FClasslikes%2F1617540583" anchor-label="FUEL_STATION_ATTRIBUTES" id="598282881%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">FUEL_STATION_ATTRIBUTES</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="598282881%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">FUEL_STATION_ATTRIBUTES</a></div></div><div class="brief "><p class="paragraph">Enables fuel attributes to be returned by Offline Search engine.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1963170239%2FClasslikes%2F1617540583" anchor-label="OFFLINE_BUS_ROUTING" id="-1963170239%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">OFFLINE_BUS_ROUTING</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1963170239%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">OFFLINE_BUS_ROUTING</a></div></div><div class="brief "><p class="paragraph">Map data that is used to calculate bus routes. When not set, the <code class="lang-kotlin">OfflineRoutingEngine</code> may not be able to calculate routes with <code class="lang-kotlin">BusOptions</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1086334730%2FClasslikes%2F1617540583" anchor-label="JUNCTION_VIEW_3X4" id="-1086334730%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">JUNCTION_VIEW_3X4</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1086334730%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">JUNCTION_VIEW_3X4</a></div></div><div class="brief "><p class="paragraph">Map data that provides junction view images and assets with aspect ratio 3x4. This will also provide common assets that do not depend on specific aspect ratio. By default this feature is disabled.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-978212889%2FClasslikes%2F1617540583" anchor-label="JUNCTION_VIEW_16X9" id="-978212889%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">JUNCTION_VIEW_16X9</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-978212889%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">JUNCTION_VIEW_16X9</a></div></div><div class="brief "><p class="paragraph">Map data that provides junction view images and assets with aspect ratio 16x9. This will also provide common assets that do not depend on specific aspect ratio. By default this feature is disabled.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1933088270%2FClasslikes%2F1617540583" anchor-label="JUNCTION_SIGN_3X4" id="1933088270%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">JUNCTION_SIGN_3X4</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1933088270%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">JUNCTION_SIGN_3X4</a></div></div><div class="brief "><p class="paragraph">Map data that provides junction sign images with aspect ratio 3x4. By default this feature is disabled.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-431648177%2FClasslikes%2F1617540583" anchor-label="JUNCTION_SIGN_3X5" id="-431648177%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">JUNCTION_SIGN_3X5</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-431648177%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">JUNCTION_SIGN_3X5</a></div></div><div class="brief "><p class="paragraph">Map data that provides junction sign images with aspect ratio 3x5. By default this feature is disabled.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-471168562%2FClasslikes%2F1617540583" anchor-label="JUNCTION_SIGN_4X3" id="-471168562%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">JUNCTION_SIGN_4X3</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-471168562%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">JUNCTION_SIGN_4X3</a></div></div><div class="brief "><p class="paragraph">Map data that provides junction sign images with aspect ratio 4x3. By default this feature is disabled.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-945194545%2FClasslikes%2F1617540583" anchor-label="JUNCTION_SIGN_5X3" id="-945194545%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">JUNCTION_SIGN_5X3</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-945194545%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">JUNCTION_SIGN_5X3</a></div></div><div class="brief "><p class="paragraph">Map data that provides junction sign images with aspect ratio 5x3. By default this feature is disabled. Feature enables following OCM layer groups:</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1865380401%2FClasslikes%2F1617540583" anchor-label="JUNCTION_SIGN_16X9" id="-1865380401%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">JUNCTION_SIGN_16X9</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1865380401%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">JUNCTION_SIGN_16X9</a></div></div><div class="brief "><p class="paragraph">Map data that provides junction sign images with aspect ratio 16x9. By default this feature is disabled.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-950791797%2FClasslikes%2F1617540583" anchor-label="TERRAIN" id="-950791797%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">TERRAIN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-950791797%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">TERRAIN</a></div></div><div class="brief "><p class="paragraph">Map data that provides topography information. The related map feature  with mode is enabled by default on topo map schemes. It is disabled by default on all other schemes.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1335322568%2FClasslikes%2F1617540583" anchor-label="DETAILED_TERRAIN" id="-1335322568%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">DETAILED_TERRAIN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1335322568%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">DETAILED_TERRAIN</a></div></div><div class="brief "><p class="paragraph">Map data that provides detailed topography information. By default this feature is disabled. Feature enables following OCM layer groups:</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-408889849%2FClasslikes%2F1617540583" anchor-label="ADAS" id="-408889849%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">ADAS</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-408889849%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">ADAS</a></div></div><div class="brief "><p class="paragraph">Map data which provides ADAS information which includes slope, elevation and curvature information. By default this feature is disabled. Feature enables following OCM layer groups:</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="338062664%2FClasslikes%2F1617540583" anchor-label="EHORIZON" id="338062664%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">EHORIZON</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="338062664%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">EHORIZON</a></div></div><div class="brief "><p class="paragraph">Map data which provides information about the parts of foreign segments in a tile, where a foreign segment is a segment that is stored in another tile but intersects the current tile. By default this feature is disabled. Feature enables following OCM layer groups:</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="978453493%2FClasslikes%2F1617540583" anchor-label="RDS_TRAFFIC" id="978453493%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">RDS_TRAFFIC</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="978453493%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">RDS_TRAFFIC</a></div></div><div class="brief "><p class="paragraph">Map data that provides traffic broadcast functionality using RDS-TMC format. It should be used when there is no internet connection, so that the routing module can utilize traffic data coming over the radio channel to build a route in the offline mode. Feature enables following OCM layer groups:</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="1266042444%2FProperties%2F1617540583" anchor-label="entries" id="1266042444%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-entries"><span><span>entries</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1266042444%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-entries">entries</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html">EnumEntries</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">LayerConfiguration.Feature</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Returns a representation of an immutable list of all enum entries, in the order they're declared.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-583498677%2FProperties%2F1617540583" anchor-label="value" id="-583498677%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-value"><span><span>value</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-583498677%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-value">value</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="890188496%2FFunctions%2F1617540583" anchor-label="valueOf" id="890188496%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-value-of"><span>value</span><wbr></wbr><span><span>Of</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="890188496%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-value-of"><span class="token function">valueOf</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">value<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">LayerConfiguration.Feature</a></div><div class="brief "><p class="paragraph">Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="657664988%2FFunctions%2F1617540583" anchor-label="values" id="657664988%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-values"><span><span>values</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="657664988%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-values"><span class="token function">values</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">LayerConfiguration.Feature</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Returns an array containing the constants of this enum type, in the order they're declared.</p></div></div></div>
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
