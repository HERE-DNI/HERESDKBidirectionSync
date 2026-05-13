---
title: "MapLayerPriorityBuilder"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>MapLayerPriorityBuilder</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.mapview/MapLayerPriorityBuilder///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.mapview</a><span class="delimiter">/</span><span class="current">MapLayerPriorityBuilder</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Map</span><wbr></wbr><span>Layer</span><wbr></wbr><span>Priority</span><wbr></wbr><span><span>Builder</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">MapLayerPriorityBuilder</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a></div><p class="paragraph">MapLayerPriorityBuilder is an interface used to define the rendering priority of a layer and its categories, relative to other layers or layer-category pairs.</p><p class="paragraph">Map layers are rendered in an order according to specified priorities. Rendering order of elements in a single map layer can be controlled with categories. Layer names are unique, and category names have to be unique within a layer. The layer's default, main category is unnamed.</p><p class="paragraph">The concept of 'category' is tightly linked to styling. The idea behind category is that one should be able to style separately elements in a map layer. Take, for instance, roads. If one wants to style separately the bridges it will create a category 'bridges' and style it accordingly in the style file. If the user does not intend to or cannot style elements of the layer diffenrently then it should opt for a layer with only the default category (e.g. raster layer).</p><p class="paragraph">One way to define layers' priorities is by using a layer priority list in the scene configuration.</p><p class="paragraph">For example, a priority list in a scene configuration could define:</p><ul><li><p class="paragraph">background</p></li><li><p class="paragraph">water</p></li><li><p class="paragraph">roads:outline</p></li><li><p class="paragraph">roads</p></li><li><p class="paragraph">labels</p></li></ul><p class="paragraph">This means layer &quot;background&quot; is rendered first. Next up is layer &quot;water&quot;. Then category &quot;outline&quot; of layer &quot;roads&quot;, followed by the main category of layer &quot;roads&quot;. Layer &quot;labels&quot; is then rendered last.</p><p>
Now let's consider a newly created layer 'zone' and its categories:<ul><li><p class="paragraph">zone</p></li><li><p class="paragraph">zone:background</p></li><li><p class="paragraph">zone:lines-outline</p></li><li><p class="paragraph">zone:lines</p></li></ul><p class="paragraph">The user wants to alter the rendering order so that it looks like:</p><ul><li><p class="paragraph">background</p></li><li><p class="paragraph">water</p></li><li><p class="paragraph">zone:background</p></li><li><p class="paragraph">zone</p></li><li><p class="paragraph">road:outline</p></li><li><p class="paragraph">road</p></li><li><p class="paragraph">zone:lines-outline</p></li><li><p class="paragraph">zone:lines</p></li><li><p class="paragraph">labels</p></li></ul><p class="paragraph">This could be achieved with the help of the MapLayerPriorityBuilder and a sequence of calls to its <code class="lang-kotlin">renderedBeforeLayer()</code> and <code class="lang-kotlin">renderedAfterLayer()</code> member functions.</p><p class="paragraph">Note that the order of calls matters and one can use a previously defined layer or category as a reference:</p><p class="paragraph">In case an empty MapLayerPriority without any ordering commands is built, it is assumed that the target layer is going to be rendered last.</p><p class="paragraph">Due to a current limitation for point map layers, the mentioned APIs to control the rendering order are not implemented. All labels will be rendered within the &quot;labels&quot; layer, defined in the scene configuration file. By default, all labels rendered by a point map layer are rendered last and no overlapping is allowed. The following categories can be used to have a different behaviour:</p><ul><li><p class="paragraph">'custom-labels' A label should be rendered first, is allowed to overlap with other labels of the same category and block map labels.</p></li><li><p class="paragraph">'custom-labels-no-self-overlap' A label should be rendered after 'custom-labels', is not allowed to overlap with other labels of the same categoty and block map labels.</p></li><li><p class="paragraph">'custom-labels-overlap-all' A label should be rendered last, is allowed to overlap all predefined categories, also map labels. These categories are configured accordingly in the basic map scene configurations. Category assignment to features can be done in the style based on data attributes. The category assignment can be done for all types of data: points, lines, polygons.</p></li></ul></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="-1694501189%2FConstructors%2F1617540583" anchor-label="MapLayerPriorityBuilder" id="-1694501189%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-map-layer-priority-builder.html"><span>Map</span><wbr></wbr><span>Layer</span><wbr></wbr><span>Priority</span><wbr></wbr><span><span>Builder</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1694501189%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates an instance of the layer priority builder interface.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="829797604%2FClasslikes%2F1617540583" anchor-label="Companion" id="829797604%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="829797604%2FClasslikes%2F1617540583"></span>
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
        <div class="table"><a data-name="1959036143%2FFunctions%2F1617540583" anchor-label="build" id="1959036143%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="build.html"><span><span>build</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1959036143%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="build.html"><span class="token function">build</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-map-layer-priority/index.html">MapLayerPriority</a></div><div class="brief "><p class="paragraph">Constructs a MapLayerPriority. The builder is then empty and can be re-used to generate a new MapLayerPriority.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="141529441%2FFunctions%2F1617540583" anchor-label="inGroup" id="141529441%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="in-group.html"><span>in</span><wbr></wbr><span><span>Group</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="141529441%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="in-group.html"><span class="token function">inGroup</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">group<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">MapLayerPriorityBuilder</a></div><div class="brief "><p class="paragraph">Sets the group for which a priority could be defined with the next call to the functions {@code renderedFirst|Last|BeforeLayer|AfterLayer}. When a group is set, the next defined priority is relative to the layers and layer categories inside this group. The references (i.e. 'referenceLayer' and 'referenceCategory') of the priority are only searched inside the group. Only one group or no group can be defined per layer priority and layer category priority, however, different layers can set priorities for the same group. After a priority is defined by calling one of the aforementioned functions, the current group is cleared and the builder refers again to the global layer list in the scene. Note that a group needs to exist when the built <a href="../-map-layer-priority/index.html">com.here.sdk.mapview.MapLayerPriority</a> is used during a <a href="../-map-layer-builder/build.html">com.here.sdk.mapview.MapLayerBuilder.build</a> or <a href="../-map-layer/set-priority.html">com.here.sdk.mapview.MapLayer.setPriority</a>, otherwise the priority cannot be applied and the layer will render nothing to the group. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1800058663%2FFunctions%2F1617540583" anchor-label="renderedAfterLayer" id="1800058663%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="rendered-after-layer.html"><span>rendered</span><wbr></wbr><span>After</span><wbr></wbr><span><span>Layer</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1800058663%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="rendered-after-layer.html"><span class="token function">renderedAfterLayer</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">referenceLayer<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">MapLayerPriorityBuilder</a></div><div class="brief "><p class="paragraph">Sets the priority as rendered after the last one from the referenceLayer and its categories. Applies to the layer itself or the category pointed to by the preceding call to <a href="with-category.html">com.here.sdk.mapview.MapLayerPriorityBuilder.withCategory</a>. Notice that the order of calls to the functions {@code renderedFirst|Last|Before|After} matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category 'C' after layer 'L' would be overridden by the priority to render layer category 'C' before layer 'L' when building something like</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="rendered-after-layer.html"><span class="token function">renderedAfterLayer</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">referenceLayer<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token punctuation">, </span></span><span class="parameter ">referenceCategory<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">MapLayerPriorityBuilder</a></div><div class="brief "><p class="paragraph">Sets the priority as rendered after the referenceCategory of the referenceLayer. Applies to the layer itself or the category pointed to by the preceding call to <a href="with-category.html">com.here.sdk.mapview.MapLayerPriorityBuilder.withCategory</a>. Notice that the order of calls to the functions {@code renderedFirst|Last|Before|After} matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category 'C' after layer 'L' would be overridden by the priority to render layer category 'C' before layer 'L' when building something like</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-528700639%2FFunctions%2F1617540583" anchor-label="renderedBeforeLayer" id="-528700639%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="rendered-before-layer.html"><span>rendered</span><wbr></wbr><span>Before</span><wbr></wbr><span><span>Layer</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-528700639%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="rendered-before-layer.html"><span class="token function">renderedBeforeLayer</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">referenceLayer<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">MapLayerPriorityBuilder</a></div><div class="brief "><p class="paragraph">Sets the priority as rendered before the first one from the referenceLayer and its categories. Applies to the layer itself or the category pointed to by the preceding call to <a href="with-category.html">com.here.sdk.mapview.MapLayerPriorityBuilder.withCategory</a>. Notice that the order of calls to the functions {@code renderedFirst|Last|Before|After} matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category 'C' after layer 'L' would be overridden by the priority to render layer category 'C' before layer 'L' when building something like</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="rendered-before-layer.html"><span class="token function">renderedBeforeLayer</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">referenceLayer<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token punctuation">, </span></span><span class="parameter ">referenceCategory<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">MapLayerPriorityBuilder</a></div><div class="brief "><p class="paragraph">Sets the priority as rendered before the referenceCategory of the referenceLayer. Applies to the layer itself or the category pointed to by the preceding call to <a href="with-category.html">com.here.sdk.mapview.MapLayerPriorityBuilder.withCategory</a>. Notice that the order of calls to the functions {@code renderedFirst|Last|Before|After} matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category 'C' after layer 'L' would be overridden by the priority to render layer category 'C' before layer 'L' when building something like</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-302913278%2FFunctions%2F1617540583" anchor-label="renderedFirst" id="-302913278%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="rendered-first.html"><span>rendered</span><wbr></wbr><span><span>First</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-302913278%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="rendered-first.html"><span class="token function">renderedFirst</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">MapLayerPriorityBuilder</a></div><div class="brief "><p class="paragraph">Sets the priority as rendered before all layers and categories. Applies to the layer itself or the category pointed to by the preceding call to <a href="with-category.html">com.here.sdk.mapview.MapLayerPriorityBuilder.withCategory</a>. Notice that the order of calls to the functions {@code renderedFirst|Last|Before|After} matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category 'C' after layer 'L' would be overridden by the priority to render layer category 'C' before layer 'L' when building something like</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1863041362%2FFunctions%2F1617540583" anchor-label="renderedLast" id="1863041362%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="rendered-last.html"><span>rendered</span><wbr></wbr><span><span>Last</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1863041362%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="rendered-last.html"><span class="token function">renderedLast</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">MapLayerPriorityBuilder</a></div><div class="brief "><p class="paragraph">Sets the priority as rendered after all layers and categories. Applies to the layer itself or the category pointed to by the preceding call to <a href="with-category.html">com.here.sdk.mapview.MapLayerPriorityBuilder.withCategory</a>. Notice that the order of calls to the functions {@code renderedFirst|Last|Before|After} matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category 'C' after layer 'L' would be overridden by the priority to render layer category 'C' before layer 'L' when building something like</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="536824107%2FFunctions%2F1617540583" anchor-label="withCategory" id="536824107%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-category.html"><span>with</span><wbr></wbr><span><span>Category</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="536824107%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-category.html"><span class="token function">withCategory</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">category<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">MapLayerPriorityBuilder</a></div><div class="brief "><p class="paragraph">Sets the layer category for which a priority could be defined with the next call to the functions {@code renderedFirst|Last|BeforeLayer|AfterLayer}. After a priority is defined by calling one of the aforementioned functions, the current category is cleared and the builder refers again to the layer itself.</p></div></div></div>
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
