---
title: "MapMarker3D"
slug: "sdk-for-flutter-navigate"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>MapMarker3D</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.mapview/MapMarker3D///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.mapview</a><span class="delimiter">/</span><span class="current">MapMarker3D</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Map</span><wbr></wbr><span><span>Marker3D</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">MapMarker3D</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a></div><p class="paragraph">Represents a 3D shape drawn on the map at specified geodetic coordinates.</p><p class="paragraph">It can have a solid color or be textured, depending on the data from <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapMarker3DModel</a>.</p><p class="paragraph">By default, a 3D marker is drawn on top of all map content, including 3D map elements like extruded buildings or 3D landmarks. This can be changed by enabling depth check using <a href="sdk-for-flutter-explore-is-depth-check-enabled">com.here.sdk.mapview.MapMarker3D.isDepthCheckEnabled</a>.</p><p class="paragraph">The display of a 3D marker is only guaranteed in case its origin is within the viewport. At the moment, this is a known limitation that mostly affects a 3D marker that is visually large and covers a sizeable part of the viewport.</p><h1 class="">Sizing and scaling</h1><p class="paragraph">Two aspects determine how big the <code class="lang-kotlin">MapMarker3D</code> will be on the screen and how will it behave when the map is zoomed in and out.</p><p class="paragraph">The first, and most impactful is <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.RenderSize.Unit</a>, which specifies how the vertex coordinates of the 3D model are interpreted. Most importantly, it specifies whether the 3D model is placed in world or screen coordinate space.</p><p class="paragraph"><a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.RenderSize.Unit.METERS</a> will make the 3D model use world coordinate space, meaning that it will change size together with the map when it is zoomed in and out.</p><p class="paragraph"><a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.RenderSize.Unit.PIXELS</a> makes the 3D model use screen coordinate space, meaning that it will have constant size on the screen regardless of how the map zoom changes. So a simple 10 by 10 (in model space) rectangle will have a size of 10 by 10 pixels on the screen.</p><p class="paragraph"><a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.RenderSize.Unit.DENSITY_INDEPENDENT_PIXELS</a> is similar to pixels, but the resulting size will take into account the pixel density of the display, meaning that physical size on the screen will be approximately the same regardless of the size or resolution of the display.</p><p class="paragraph">The second aspect that determines size of <code class="lang-kotlin">MapMarker3D</code> is scale. It can be specified at construction time and can be changed later at any time using <a href="sdk-for-flutter-explore-scale">com.here.sdk.mapview.MapMarker3D.scale</a>.</p><h1 class="">Modifying at runtime</h1><p class="paragraph">A 3D marker can be moved around a map by updating its coordinates using <a href="sdk-for-flutter-explore-coordinates">com.here.sdk.mapview.MapMarker3D.coordinates</a>.</p><p class="paragraph">Altitude component of the coordinates, if set, controls 3D marker's elevation above ground. If not set, the 3D marker is placed at ground level.</p><p class="paragraph">Its orientation is specified by bearing, pitch and roll and can be changed by using <a href="sdk-for-flutter-explore-bearing">com.here.sdk.mapview.MapMarker3D.bearing</a>, <a href="sdk-for-flutter-explore-pitch">com.here.sdk.mapview.MapMarker3D.pitch</a> and <a href="sdk-for-flutter-explore-roll">com.here.sdk.mapview.MapMarker3D.roll</a>.</p><h1 class="">Flat marker</h1><p class="paragraph">A flat marker is a special case of a 3D marker, where the 3D shape being drawn is a simple textured rectangle. In essence it's an image drawn &quot;on the ground&quot;. Such 3D marker can be conveniently created using com.here.sdk.mapview.MapMarker3D.MapMarker3D constructor. Of course, once created, it can be rotated to face any direction.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="-1108773546%2FConstructors%2F1617540583" anchor-label="MapMarker3D" id="-1108773546%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-map-marker3-d"><span>Map</span><wbr></wbr><span><span>Marker3D</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1108773546%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">at<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a><span class="token punctuation">, </span></span><span class="parameter ">model<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMarker3DModel</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates an instance of a 3D marker.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">at<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a><span class="token punctuation">, </span></span><span class="parameter ">image<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapImage</a><span class="token punctuation">, </span></span><span class="parameter ">scale<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token punctuation">, </span></span><span class="parameter ">unit<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">RenderSize.Unit</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a flat marker from provided map image.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">at<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a><span class="token punctuation">, </span></span><span class="parameter ">model<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMarker3DModel</a><span class="token punctuation">, </span></span><span class="parameter ">scale<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates an instance of a 3D marker with scale factor.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">at<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a><span class="token punctuation">, </span></span><span class="parameter ">model<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMarker3DModel</a><span class="token punctuation">, </span></span><span class="parameter ">scale<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token punctuation">, </span></span><span class="parameter ">unit<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">RenderSize.Unit</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new 3D marker at given world coordinates, using the supplied 3D model.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="1997741279%2FClasslikes%2F1617540583" anchor-label="Companion" id="1997741279%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1997741279%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">object </span><a href="sdk-for-flutter-explore-index">Companion</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="-2070516118%2FProperties%2F1617540583" anchor-label="bearing" id="-2070516118%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-bearing"><span><span>bearing</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2070516118%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-bearing">bearing</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief "><p class="paragraph">The bearing of the 3D model in degrees, from the true North in clockwise direction. The bearing axis is perpendicular to the ground and passes through the 3D marker's location. The Z-axis of the model is aligned with bearing axis.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="418326333%2FProperties%2F1617540583" anchor-label="coordinates" id="418326333%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-coordinates"><span><span>coordinates</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="418326333%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-coordinates">coordinates</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a></div><div class="brief "><p class="paragraph">The position of the 3D marker on the map corresponding to the origin of the 3D marker model coordinate system. The altitude component of the coordinates, if set, controls 3D marker's elevation above ground. If not set, the 3D marker is placed at ground level.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="629855910%2FProperties%2F1617540583" anchor-label="isDepthCheckEnabled" id="629855910%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-is-depth-check-enabled"><span>is</span><wbr></wbr><span>Depth</span><wbr></wbr><span>Check</span><wbr></wbr><span><span>Enabled</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="629855910%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-is-depth-check-enabled">isDepthCheckEnabled</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Determines whether the depth of the 3D marker's vertices is considered during rendering. If set to <code class="lang-kotlin">false</code>, the 3D marker will always appear in front of any other map objects. If set to <code class="lang-kotlin">true</code> the 3D marker might be occluded by other map objects like extruded buildings.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1208889257%2FProperties%2F1617540583" anchor-label="isRenderInternalsEnabled" id="-1208889257%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-is-render-internals-enabled"><span>is</span><wbr></wbr><span>Render</span><wbr></wbr><span>Internals</span><wbr></wbr><span><span>Enabled</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1208889257%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-is-render-internals-enabled">isRenderInternalsEnabled</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Indicates whether to render internal geometry of a 3D marker occluded by its front facing polygons. Default value is <code class="lang-kotlin">false</code>. Can be used with translucent 3D marker.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="340802611%2FProperties%2F1617540583" anchor-label="metadata" id="340802611%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-metadata"><span><span>metadata</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="340802611%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-metadata">metadata</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Metadata</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The <a href="sdk-for-flutter-explore-index">com.here.sdk.core.Metadata</a> instance attached to this 3D marker.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1653219501%2FProperties%2F1617540583" anchor-label="opacity" id="1653219501%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-opacity"><span><span>opacity</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1653219501%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-opacity">opacity</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief "><p class="paragraph">The opacity factor adjusting the opacity of a 3D marker. The factor is applied to the alpha channel of the resulting texture of the marker. Default value is 1.0 meaning marker is displayed with the default opacity of the texture image or the specified fill color specified in <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapMarker3DModel</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-328411688%2FProperties%2F1617540583" anchor-label="pitch" id="-328411688%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-pitch"><span><span>pitch</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-328411688%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-pitch">pitch</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief "><p class="paragraph">The pitch of the 3D model in degrees. The pitch axis is parallel to the ground, passes through the location of the 3D marker and aligns with the longitude axis if the bearing is 0. However, this axis rotates with the 3D marker according to the bearing value. Negative values cause the top of the 3D marker to lean forward. The X-axis of the model is aligned with pitch axis.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="152589605%2FProperties%2F1617540583" anchor-label="roll" id="152589605%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-roll"><span><span>roll</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="152589605%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-roll">roll</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief "><p class="paragraph">The roll angle of the 3D model in degrees. The roll axis is parallel to the ground, passes through the 3D marker's location and is aligned initially with the true North. However, when the bearing changes, it rotates around the bearing axis with the 3D marker. Positive/negative values cause a clockwise/counterclockwise rotation when viewing along the axis in the direction of the true North. The Y-axis of the model is aligned with the roll axis.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="358453006%2FProperties%2F1617540583" anchor-label="scale" id="358453006%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-scale"><span><span>scale</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="358453006%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-scale">scale</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief "><p class="paragraph">Scale factor applied to the 3D model before rendering.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1089044474%2FProperties%2F1617540583" anchor-label="visibilityRanges" id="1089044474%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-visibility-ranges"><span>visibility</span><wbr></wbr><span><span>Ranges</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1089044474%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-visibility-ranges">visibilityRanges</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">MapMeasureRange</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">The list of visibility ranges. The 3D marker is visible only inside these map measure ranges. A range is half open - \[minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range.</p></div></div></div>
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
