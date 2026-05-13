---
title: "LocationIndicator"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-mapview-location-indicator"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>LocationIndicator</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.mapview/LocationIndicator///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.mapview</a><span class="delimiter">/</span><span class="current">LocationIndicator</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Location</span><wbr></wbr><span><span>Indicator</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">LocationIndicator</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a></div><p class="paragraph">Graphical object to represent the location of the user on the map.</p><p class="paragraph">It is either a green dot for pedestrian style or a triangular arrow for vehicle navigation style. This style can be changed by <a href="location-indicator-style.html">com.here.sdk.mapview.LocationIndicator.locationIndicatorStyle</a></p><p class="paragraph">The location is made available to an instance of this class by calling <a href="update-location.html">com.here.sdk.mapview.LocationIndicator.updateLocation</a> or <a href="update-location.html">com.here.sdk.mapview.LocationIndicator.updateLocation</a>.</p><p class="paragraph">Use <a href="enable.html">com.here.sdk.mapview.LocationIndicator.enable</a> to add this object to the map and <a href="disable.html">com.here.sdk.mapview.LocationIndicator.disable</a> to remove it.</p><p class="paragraph">Take care that the location indicator is not accidentally added to the map view multiple times for example when the android activity is recreated after an orientation change.</p><p class="paragraph">Note: The LocationIndicator is always rendered at a fixed altitude near 0. Changing the MapCamera to look at geographic coordinates with an altitude that is higher can cause the following behavior: If the MapCamera angle is tilted and altitude is too high, the LocationIndicator can unexpectedly disappear from the viewport due to the new perspective.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="1171485068%2FConstructors%2F1617540583" anchor-label="LocationIndicator" id="1171485068%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-location-indicator.html"><span>Location</span><wbr></wbr><span><span>Indicator</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1171485068%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates an instance of LocationIndicator.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">mapView<span class="token operator">: </span><a href="../-map-view-base/index.html">MapViewBase</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates an instance of LocationIndicator and adds it to provided <a href="../-map-view-base/index.html">com.here.sdk.mapview.MapViewBase</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="462929292%2FClasslikes%2F1617540583" anchor-label="Companion" id="462929292%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="462929292%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">object </span><a href="-companion/index.html">Companion</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1003080456%2FClasslikes%2F1617540583" anchor-label="IndicatorStyle" id="1003080456%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-indicator-style/index.html"><span>Indicator</span><wbr></wbr><span><span>Style</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1003080456%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-indicator-style/index.html">IndicatorStyle</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-indicator-style/index.html">LocationIndicator.IndicatorStyle</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">The predefined styles for the location indicator which are pedestrian and navigation mode.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2134659606%2FClasslikes%2F1617540583" anchor-label="MarkerType" id="2134659606%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-marker-type/index.html"><span>Marker</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2134659606%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-marker-type/index.html">MarkerType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-marker-type/index.html">LocationIndicator.MarkerType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Enum to identify different types of markers of the location indicator.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="-1178882014%2FProperties%2F1617540583" anchor-label="isAccuracyVisualized" id="-1178882014%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="is-accuracy-visualized.html"><span>is</span><wbr></wbr><span>Accuracy</span><wbr></wbr><span><span>Visualized</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1178882014%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="is-accuracy-visualized.html">isAccuracyVisualized</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Whether the horizontal accuracy is visualized by scaling the accuracy indicator halo.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1084603547%2FProperties%2F1617540583" anchor-label="isActive" id="-1084603547%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="is-active.html"><span>is</span><wbr></wbr><span><span>Active</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1084603547%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="is-active.html">isActive</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">A Boolean value that determines whether the active on inactive version of location indicator is shown.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1676927006%2FProperties%2F1617540583" anchor-label="locationIndicatorStyle" id="1676927006%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="location-indicator-style.html"><span>location</span><wbr></wbr><span>Indicator</span><wbr></wbr><span><span>Style</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1676927006%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="location-indicator-style.html">locationIndicatorStyle</a><span class="token operator">: </span><a href="-indicator-style/index.html">LocationIndicator.IndicatorStyle</a></div><div class="brief "><p class="paragraph">The visual style of location indicator. By default, it is set to <a href="-indicator-style/-n-a-v-i-g-a-t-i-o-n/index.html">com.here.sdk.mapview.LocationIndicator.IndicatorStyle.NAVIGATION</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1651430902%2FProperties%2F1617540583" anchor-label="materialReflectivity" id="-1651430902%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="material-reflectivity.html"><span>material</span><wbr></wbr><span><span>Reflectivity</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1651430902%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="material-reflectivity.html">materialReflectivity</a><span class="token operator">: </span><a href="../-material-reflectivity/index.html">MaterialReflectivity</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The material reflectivity properties of the location indicator. Enables per‑pixel lighting for all internal markers (navigation, pedestrian, inactive variants) and the halo when assigned. While <code class="lang-kotlin">materialReflectivity</code> is non‑null the markers are shaded by scene lights using the provided ambient / diffuse factors. When set back to <code class="lang-kotlin">null</code>, lighting is disabled and markers revert to unlit (emissive) rendering.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1289156454%2FProperties%2F1617540583" anchor-label="opacity" id="-1289156454%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="opacity.html"><span><span>opacity</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1289156454%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="opacity.html">opacity</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief "><p class="paragraph">The factor applied to the alpha channel of both the location indicator's texture and the accuracy indicator's halo color. Default value is 1.0 which means location indicator is displayed with the default alpha channel of the texture.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="2063786077%2FFunctions%2F1617540583" anchor-label="disable" id="2063786077%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="disable.html"><span><span>disable</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2063786077%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="disable.html"><span class="token function">disable</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">This function removes <a href="index.html">com.here.sdk.mapview.LocationIndicator</a> from map view. If <a href="index.html">com.here.sdk.mapview.LocationIndicator</a> was not added to any map view yet, this function does nothing.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-884957582%2FFunctions%2F1617540583" anchor-label="enable" id="-884957582%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="enable.html"><span><span>enable</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-884957582%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="enable.html"><span class="token function">enable</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">mapView<span class="token operator">: </span><a href="../-map-view-base/index.html">MapViewBase</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Enables <a href="index.html">com.here.sdk.mapview.LocationIndicator</a> for provided <a href="../-map-view-base/index.html">com.here.sdk.mapview.MapViewBase</a>. If <a href="index.html">com.here.sdk.mapview.LocationIndicator</a> is already enabled (added to map view) for passed map view, this function does nothing. If <a href="index.html">com.here.sdk.mapview.LocationIndicator</a> is added to different <a href="../-map-view-base/index.html">com.here.sdk.mapview.MapViewBase</a>, this function removes first <a href="index.html">com.here.sdk.mapview.LocationIndicator</a> from previous map view before adding to new one.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1147246538%2FFunctions%2F1617540583" anchor-label="getHaloColor" id="-1147246538%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-halo-color.html"><span>get</span><wbr></wbr><span>Halo</span><wbr></wbr><span><span>Color</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1147246538%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-halo-color.html"><span class="token function">getHaloColor</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">style<span class="token operator">: </span><a href="-indicator-style/index.html">LocationIndicator.IndicatorStyle</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core/-color/index.html">Color</a></div><div class="brief "><p class="paragraph">Retrieves the color of the accuracy indicator halo for the requested IndicatorStyle. The default color is a translucent turquoise (rgba(0, 199, 194, 76)) for all IndicatorStyle settings.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-651078348%2FFunctions%2F1617540583" anchor-label="setHaloColor" id="-651078348%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="set-halo-color.html"><span>set</span><wbr></wbr><span>Halo</span><wbr></wbr><span><span>Color</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-651078348%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="set-halo-color.html"><span class="token function">setHaloColor</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">style<span class="token operator">: </span><a href="-indicator-style/index.html">LocationIndicator.IndicatorStyle</a><span class="token punctuation">, </span></span><span class="parameter ">color<span class="token operator">: </span><a href="../../com.here.sdk.core/-color/index.html">Color</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Sets the color of the accuracy indicator halo for a given style.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1160386236%2FFunctions%2F1617540583" anchor-label="setMarker3dModel" id="1160386236%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="set-marker3d-model.html"><span>set</span><wbr></wbr><span>Marker3d</span><wbr></wbr><span><span>Model</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1160386236%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="set-marker3d-model.html"><span class="token function"><strike>setMarker3dModel</strike></span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">model<span class="token operator">: </span><a href="../-map-marker3-d-model/index.html">MapMarker3DModel</a><span class="token punctuation">, </span></span><span class="parameter ">scale<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token punctuation">, </span></span><span class="parameter ">type<span class="token operator">: </span><a href="-marker-type/index.html">LocationIndicator.MarkerType</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Sets the MapMarker3DModel asset to be displayed as location indicator for a specified type. The 3D model should be oriented with y axis up and thus standing on the x/z plane where the z axis is the depth. The direction in which the location indicator is pointing is the positive z axis. Please note that only MapMarker3DModel created from *.obj files are supported. Models created from Mesh will be ignored.</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="set-marker3d-model.html"><span class="token function">setMarker3dModel</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">model<span class="token operator">: </span><a href="../-map-marker3-d-model/index.html">MapMarker3DModel</a><span class="token punctuation">, </span></span><span class="parameter ">scale<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token punctuation">, </span></span><span class="parameter ">type<span class="token operator">: </span><a href="-marker-type/index.html">LocationIndicator.MarkerType</a><span class="token punctuation">, </span></span><span class="parameter ">renderSizeUnit<span class="token operator">: </span><a href="../-render-size/-unit/index.html">RenderSize.Unit</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Sets the <a href="../-map-marker3-d-model/index.html">com.here.sdk.mapview.MapMarker3DModel</a> asset to be displayed as location indicator for a specified type. The 3D model should be oriented with y axis up and thus standing on the x/z plane where the z axis is the depth. The direction in which the location indicator is pointing is the positive z axis. Please note that only <a href="../-map-marker3-d-model/index.html">com.here.sdk.mapview.MapMarker3DModel</a> created from <code class="lang-kotlin">obj</code> files are supported. Models created from Mesh will be ignored.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-973659045%2FFunctions%2F1617540583" anchor-label="updateLocation" id="-973659045%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="update-location.html"><span>update</span><wbr></wbr><span><span>Location</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-973659045%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="update-location.html"><span class="token function">updateLocation</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">location<span class="token operator">: </span><a href="../../com.here.sdk.core/-location/index.html">Location</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Updates the indicator to a new location. If accuracy visualized is set to <code class="lang-kotlin">true</code> the field <a href="../../com.here.sdk.core/-location/horizontal-accuracy-in-meters.html">com.here.sdk.core.Location.horizontalAccuracyInMeters</a> determines the size of the accuracy indicator halo.</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="update-location.html"><span class="token function">updateLocation</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">location<span class="token operator">: </span><a href="../../com.here.sdk.core/-location/index.html">Location</a><span class="token punctuation">, </span></span><span class="parameter ">cameraUpdate<span class="token operator">: </span><a href="../-map-camera-update/index.html">MapCameraUpdate</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Updates the indicator to a new location and applies a camera update at the same time.</p></div></div></div>
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
