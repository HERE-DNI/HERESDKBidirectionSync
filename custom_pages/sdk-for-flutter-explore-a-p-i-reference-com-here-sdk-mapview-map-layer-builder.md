---
title: "MapLayerBuilder"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>MapLayerBuilder</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.mapview/MapLayerBuilder///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.mapview</a><span class="delimiter">/</span><span class="current">MapLayerBuilder</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Map</span><wbr></wbr><span>Layer</span><wbr></wbr><span><span>Builder</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">MapLayerBuilder</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a></div><p class="paragraph">MapLayerBuilder is used to add layers to a map to visualise a dataset in a programmatic way without defining it upfront in the configuration files.</p><p class="paragraph">For example, after loading a scene configuration file, the renderer is setup to draw layers in the following order:</p><ul><li><p class="paragraph">background</p></li><li><p class="paragraph">water</p></li><li><p class="paragraph">roads:outline</p></li><li><p class="paragraph">roads</p></li><li><p class="paragraph">labels</p></li></ul><p class="paragraph">Rendering order of elements in a single map layer can be controlled with categories. Layer names are unique, and category names have to be unique within a layer. The layer's default, main category is unnamed.</p><p class="paragraph">The concept of 'category' is tightly linked to styling. The idea behind category is that one should be able to style separately elements in a map layer. Take, for instance, roads. If one wants to style separately the bridges it will create a category 'bridges' and style it accordingly in the style file. If the user does not intend to or cannot style elements of the layer differently then it should opt for a layer with only the default category (e.g. for a raster layer, only the default category makes sense, since the layer has no other stylable elements apart from the raster image).</p><p class="paragraph">A new layer called 'zone' and its category 'background' can be added dynamically so that the rendering order gets modified in the following way:</p><ul><li><p class="paragraph">background</p></li><li><p class="paragraph">water</p></li><li><p class="paragraph">zone:background</p></li><li><p class="paragraph">zone</p></li><li><p class="paragraph">roads:outline</p></li><li><p class="paragraph">roads</p></li><li><p class="paragraph">labels</p></li></ul><p class="paragraph">This could be achieved with the help of the MapLayerPriorityBuilder and the MapLayerBuilder as in the following example:</p><p class="paragraph">In case no layer priority or an empty one is provided, or if a reference layer-category pair is not present in the rendering order, the layer is going to be rendered last with respect to the rendering order at the time of its creation.</p><p class="paragraph">Due to current limitations, the MapLayerPriority assignment is not implemented for point map layers. All labels will be rendered within the &quot;labels&quot; layer, defined in the scene configuration file. By default, all labels rendered by a point map layer are rendered last and no overlapping is allowed. The following categories can be used to have a different behaviour:</p><ul><li><p class="paragraph">'custom-labels' A label should be rendered first, is allowed to overlap with other labels of the same category and block map labels.</p></li><li><p class="paragraph">'custom-labels-no-self-overlap' A label should be rendered after 'custom-labels', is not allowed to overlap with other labels of the same categoty and block map labels.</p></li><li><p class="paragraph">'custom-labels-overlap-all' A label should be rendered last, is allowed to overlap all predefined categories, also map labels. These categories are configured accordingly in the basic map scene configurations. Category assignment to features can be done in the style based on data attributes. The category assignment can be done for all types of content: point, line, polygon.</p></li></ul></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="180424755%2FConstructors%2F1617540583" anchor-label="MapLayerBuilder" id="180424755%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-map-layer-builder.html"><span>Map</span><wbr></wbr><span>Layer</span><wbr></wbr><span><span>Builder</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="180424755%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates an instance of the layer builder interface.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-1015622624%2FClasslikes%2F1617540583" anchor-label="Companion" id="-1015622624%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1015622624%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">object </span><a href="-companion/index.html">Companion</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-854420914%2FClasslikes%2F1617540583" anchor-label="InstantiationErrorCode" id="-854420914%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-instantiation-error-code/index.html"><span>Instantiation</span><wbr></wbr><span>Error</span><wbr></wbr><span><span>Code</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-854420914%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-instantiation-error-code/index.html">InstantiationErrorCode</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-instantiation-error-code/index.html">MapLayerBuilder.InstantiationErrorCode</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Describes a reason for failing to build a <a href="../-map-layer/index.html">com.here.sdk.mapview.MapLayer</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-431436667%2FClasslikes%2F1617540583" anchor-label="InstantiationErrorDetails" id="-431436667%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-instantiation-error-details/index.html"><span>Instantiation</span><wbr></wbr><span>Error</span><wbr></wbr><span><span>Details</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-431436667%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-instantiation-error-details/index.html">InstantiationErrorDetails</a></div><div class="brief "><p class="paragraph">Describes the reason for failing to build a <a href="../-map-layer/index.html">com.here.sdk.mapview.MapLayer</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1117763756%2FClasslikes%2F1617540583" anchor-label="InstantiationException" id="-1117763756%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-instantiation-exception/index.html"><span>Instantiation</span><wbr></wbr><span><span>Exception</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1117763756%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-instantiation-exception/index.html">InstantiationException</a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span class="token keyword">val </span>error<span class="token operator">: </span><a href="-instantiation-error-details/index.html">MapLayerBuilder.InstantiationErrorDetails</a></span></span><span class="token punctuation">)</span> : <a href="https://developer.android.com/reference/kotlin/java/lang/Exception.html">Exception</a></div><div class="brief "><p class="paragraph">Thrown when failing to build a <a href="../-map-layer/index.html">com.here.sdk.mapview.MapLayer</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="-3235285%2FFunctions%2F1617540583" anchor-label="build" id="-3235285%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="build.html"><span><span>build</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-3235285%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="build.html"><span class="token function">build</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-map-layer/index.html">MapLayer</a></div><div class="brief "><p class="paragraph">Constructs, registers and configures a new map layer showing specified content type according to the configured parameters. After this call this instance is reset to the initial state. It could be used to build another map layer, but will not keep any previously configured properties.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-585883756%2FFunctions%2F1617540583" anchor-label="forMap" id="-585883756%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="for-map.html"><span>for</span><wbr></wbr><span><span>Map</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-585883756%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="for-map.html"><span class="token function">forMap</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">targetMap<span class="token operator">: </span><a href="../-here-map/index.html">HereMap</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">MapLayerBuilder</a></div><div class="brief "><p class="paragraph">Configures the builder to display a layer in the given map. The map is a mandatory layer creation parameter.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-209914040%2FFunctions%2F1617540583" anchor-label="withDataSource" id="-209914040%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-data-source.html"><span>with</span><wbr></wbr><span>Data</span><wbr></wbr><span><span>Source</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-209914040%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-data-source.html"><span class="token function">withDataSource</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">dataSourceName<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token punctuation">, </span></span><span class="parameter ">contentType<span class="token operator">: </span><a href="../-map-content-type/index.html">MapContentType</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">MapLayerBuilder</a></div><div class="brief "><p class="paragraph">Configures the builder to use a data source with the given name as the source of data for the layer. The datasource name and content type are mandatory layer creation parameters.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-206435757%2FFunctions%2F1617540583" anchor-label="withLoadPriority" id="-206435757%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-load-priority.html"><span>with</span><wbr></wbr><span>Load</span><wbr></wbr><span><span>Priority</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-206435757%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-load-priority.html"><span class="token function">withLoadPriority</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">loadPriority<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">MapLayerBuilder</a></div><div class="brief "><p class="paragraph">Configures the builder to set the layer load priority. Higher load priority values lead to layer being scheduled for loading before layers with lesser values.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1713879552%2FFunctions%2F1617540583" anchor-label="withMapMeasureDependentStorageLevels" id="1713879552%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-map-measure-dependent-storage-levels.html"><span>with</span><wbr></wbr><span>Map</span><wbr></wbr><span>Measure</span><wbr></wbr><span>Dependent</span><wbr></wbr><span>Storage</span><wbr></wbr><span><span>Levels</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1713879552%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-map-measure-dependent-storage-levels.html"><span class="token function">withMapMeasureDependentStorageLevels</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">mapLayerMapMeasureDependentStorageLevels<span class="token operator">: </span><a href="../-map-layer-map-measure-dependent-storage-levels/index.html">MapLayerMapMeasureDependentStorageLevels</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">MapLayerBuilder</a></div><div class="brief "><p class="paragraph">Applies a mapping from the map measure to the storage level. This mapping is used by the layer to request data for the specified storage level corresponding to the map measure from the datasource. This can be used for example to fine-tune the resolution of raster layers. Note: When the map camera is significantly tilted, the storage level is further reduced for data towards the horizon. Note: Mappings that request higher storage levels will lead to an increased number of requests to the raster tile service. Providing the map measure to storage level mapping is optional. If not provided, the default mapping will use a storage level that is for raster layers one and for others three levels lower than the zoom level, corresponding to an offset of -1 and -3.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="360885556%2FFunctions%2F1617540583" anchor-label="withName" id="360885556%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-name.html"><span>with</span><wbr></wbr><span><span>Name</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="360885556%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-name.html"><span class="token function">withName</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">name<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">MapLayerBuilder</a></div><div class="brief "><p class="paragraph">Configures builder to use the given name as a layer name. The name is a mandatory layer creation parameter.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1129423904%2FFunctions%2F1617540583" anchor-label="withPriority" id="-1129423904%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-priority.html"><span>with</span><wbr></wbr><span><span>Priority</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1129423904%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-priority.html"><span class="token function">withPriority</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">priority<span class="token operator">: </span><a href="../-map-layer-priority/index.html">MapLayerPriority</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">MapLayerBuilder</a></div><div class="brief "><p class="paragraph">Configures the builder to set the MapLayerPriority to be used by the layer.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1854013007%2FFunctions%2F1617540583" anchor-label="withStyle" id="1854013007%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-style.html"><span>with</span><wbr></wbr><span><span>Style</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1854013007%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-style.html"><span class="token function">withStyle</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">style<span class="token operator">: </span><a href="../-style/index.html">Style</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">MapLayerBuilder</a></div><div class="brief "><p class="paragraph">Configures the builder to use a style. Providing a style during layer creation is not mandatory. The style can also be set/updated after the layer creation. For more details see Custom Layer Style Reference in the documentation. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="830474128%2FFunctions%2F1617540583" anchor-label="withVisibilityRange" id="830474128%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-visibility-range.html"><span>with</span><wbr></wbr><span>Visibility</span><wbr></wbr><span><span>Range</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="830474128%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-visibility-range.html"><span class="token function">withVisibilityRange</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">visibilityRange<span class="token operator">: </span><a href="../-map-layer-visibility-range/index.html">MapLayerVisibilityRange</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">MapLayerBuilder</a></div><div class="brief "><p class="paragraph">Configures the builder to set the layer visible in the given zoom levels range. Values outside the map zoom level range (0, 24) will be ignored. Providing the visibility range is optional. If not provided, the layer will be visible on all zoom levels.</p></div></div></div>
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
