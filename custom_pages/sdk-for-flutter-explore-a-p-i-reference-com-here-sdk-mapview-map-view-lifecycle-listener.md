---
title: "MapViewLifecycleListener"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-lifecycle-listener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>MapViewLifecycleListener</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.mapview/MapViewLifecycleListener///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.mapview</a><span class="delimiter">/</span><span class="current">MapViewLifecycleListener</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Map</span><wbr></wbr><span>View</span><wbr></wbr><span>Lifecycle</span><wbr></wbr><span><span>Listener</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">interface </span><a href="index.html">MapViewLifecycleListener</a></div><p class="paragraph">Provides a mechanism for observing a lifecycle of a map view and/or implementing components whose lifecycle needs to be linked with that of a map view.</p><p class="paragraph">A configuration change that results in <code class="lang-kotlin">Activity</code> being recreated does not trigger an <a href="on-destroy.html">com.here.sdk.mapview.MapViewLifecycleListener.onDestroy</a> call. The listener will be preserved throughout the destruction and recreation of the MapView. It is safe to hold and use the <code class="lang-kotlin">MapViewBase</code> object passed in <a href="on-attach.html">com.here.sdk.mapview.MapViewLifecycleListener.onAttach</a> until <code class="lang-kotlin">onDetach()</code> or <code class="lang-kotlin">onDestroy()</code> gets called. However, it is important that the listener <i>does not</i> hold a strong reference to an <code class="lang-kotlin">Activity</code>, directly or indirectly (for example by holding a reference to a {@link MapView}. A component implementing this interface should interact with the map view only through the <code class="lang-kotlin">MapViewBase</code> object passed in <a href="on-attach.html">com.here.sdk.mapview.MapViewLifecycleListener.onAttach</a>.</p><p class="paragraph">A <code class="lang-kotlin">MapView</code> is using a <a href="https://developer.android.com/reference/android/view/SurfaceView">SurfaceView</a></p><p class="paragraph">to render its content.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="599857178%2FFunctions%2F1617540583" anchor-label="onAttach" id="599857178%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="on-attach.html"><span>on</span><wbr></wbr><span><span>Attach</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="599857178%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="on-attach.html"><span class="token function">onAttach</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">mapView<span class="token operator">: </span><a href="../-map-view-base/index.html">MapViewBase</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Called when adding <a href="index.html">com.here.sdk.mapview.MapViewLifecycleListener</a> to the map view. If the map view does not have render target attached at the time of adding the listener, then this method will be called later, after render target is attached. This means that the map view it receives is always fully initialized.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="504331425%2FFunctions%2F1617540583" anchor-label="onDestroy" id="504331425%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="on-destroy.html"><span>on</span><wbr></wbr><span><span>Destroy</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="504331425%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="on-destroy.html"><span class="token function">onDestroy</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Called when the map view to which this is attached to is destroyed. After this is called, no other <a href="index.html">com.here.sdk.mapview.MapViewLifecycleListener</a> method will be invoked. This should be used to make sure all resources are freed.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1321671308%2FFunctions%2F1617540583" anchor-label="onDetach" id="1321671308%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="on-detach.html"><span>on</span><wbr></wbr><span><span>Detach</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1321671308%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="on-detach.html"><span class="token function">onDetach</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">mapView<span class="token operator">: </span><a href="../-map-view-base/index.html">MapViewBase</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Called when removing <a href="index.html">com.here.sdk.mapview.MapViewLifecycleListener</a> from the map view. Can be used to implement the logic to remove visual components from the map view and release resources if necessary.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2024454565%2FFunctions%2F1617540583" anchor-label="onPause" id="2024454565%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="on-pause.html"><span>on</span><wbr></wbr><span><span>Pause</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2024454565%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="on-pause.html"><span class="token function">onPause</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Called when the map view to which this <a href="index.html">com.here.sdk.mapview.MapViewLifecycleListener</a> is attached to gets paused (usually when the app goes into background). This should be used by components that perform continuous updates to pause those updates until <a href="on-resume.html">com.here.sdk.mapview.MapViewLifecycleListener.onResume</a> is called.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1714692306%2FFunctions%2F1617540583" anchor-label="onResume" id="1714692306%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="on-resume.html"><span>on</span><wbr></wbr><span><span>Resume</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1714692306%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="on-resume.html"><span class="token function">onResume</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Called when the map view to which this <a href="index.html">com.here.sdk.mapview.MapViewLifecycleListener</a> is attached to gets resumed (usually when the app goes into foreground). This should be used by components that perform continuous updates to resume those updates after a previous call to <a href="on-pause.html">com.here.sdk.mapview.MapViewLifecycleListener.onPause</a>.</p></div></div></div>
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
