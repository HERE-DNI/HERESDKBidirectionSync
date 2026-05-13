---
title: "Gestures"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-gestures-gestures"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>Gestures</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.gestures/Gestures///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.gestures</a><span class="delimiter">/</span><span class="current">Gestures</span></div>
  <div class="cover ">
    <h1 class="cover"><span><span>Gestures</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">Gestures</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a></div><p class="paragraph">Use this class to process touch events from the platform and detect gesture induced actions on the map view. Please note that this class holds strong references to the gesture listeners. On Android Auto, processing touch events is not needed. Instead, gestures get detected by android auto platform and provided via callbacks. For more information see onClick, onFling and onScale methods in <a href="https://developer.android.com/reference/androidx/car/app/SurfaceCallback">https://developer.android.com/reference/androidx/car/app/SurfaceCallback</a>.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-802858935%2FClasslikes%2F1617540583" anchor-label="Companion" id="-802858935%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-802858935%2FClasslikes%2F1617540583"></span>
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
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="-2010858532%2FProperties%2F1617540583" anchor-label="doubleTapListener" id="-2010858532%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="double-tap-listener.html"><span>double</span><wbr></wbr><span>Tap</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2010858532%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="double-tap-listener.html">doubleTapListener</a><span class="token operator">: </span><a href="../-double-tap-listener/index.html">DoubleTapListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph"><a href="../-double-tap-listener/index.html">com.here.sdk.gestures.DoubleTapListener</a> that notifies when a double-tap gesture occurs.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-195465270%2FProperties%2F1617540583" anchor-label="flingHandler" id="-195465270%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="fling-handler.html"><span>fling</span><wbr></wbr><span><span>Handler</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-195465270%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="fling-handler.html">flingHandler</a><span class="token operator">: </span><a href="../-fling-handler/index.html">FlingHandler</a></div><div class="brief "><p class="paragraph">Fling handler.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1405994343%2FProperties%2F1617540583" anchor-label="longPressListener" id="1405994343%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="long-press-listener.html"><span>long</span><wbr></wbr><span>Press</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1405994343%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="long-press-listener.html">longPressListener</a><span class="token operator">: </span><a href="../-long-press-listener/index.html">LongPressListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph"><a href="../-long-press-listener/index.html">com.here.sdk.gestures.LongPressListener</a> that notifies when a long-press gesture occurs.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1328221809%2FProperties%2F1617540583" anchor-label="panListener" id="1328221809%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="pan-listener.html"><span>pan</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1328221809%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="pan-listener.html">panListener</a><span class="token operator">: </span><a href="../-pan-listener/index.html">PanListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph"><a href="../-pan-listener/index.html">com.here.sdk.gestures.PanListener</a> that notifies when a pan gesture occurs.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-733476263%2FProperties%2F1617540583" anchor-label="pinchRotateListener" id="-733476263%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="pinch-rotate-listener.html"><span>pinch</span><wbr></wbr><span>Rotate</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-733476263%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="pinch-rotate-listener.html">pinchRotateListener</a><span class="token operator">: </span><a href="../-pinch-rotate-listener/index.html">PinchRotateListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph"><a href="../-pinch-rotate-listener/index.html">com.here.sdk.gestures.PinchRotateListener</a> that notifies when a pinch-rotate gesture occurs.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="821113784%2FProperties%2F1617540583" anchor-label="scaleHandler" id="821113784%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="scale-handler.html"><span>scale</span><wbr></wbr><span><span>Handler</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="821113784%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="scale-handler.html">scaleHandler</a><span class="token operator">: </span><a href="../-scale-handler/index.html">ScaleHandler</a></div><div class="brief "><p class="paragraph">Scale handler.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1611046043%2FProperties%2F1617540583" anchor-label="scrollHandler" id="-1611046043%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="scroll-handler.html"><span>scroll</span><wbr></wbr><span><span>Handler</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1611046043%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="scroll-handler.html">scrollHandler</a><span class="token operator">: </span><a href="../-scroll-handler/index.html">ScrollHandler</a></div><div class="brief "><p class="paragraph">Scroll handler.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1704495061%2FProperties%2F1617540583" anchor-label="tapListener" id="-1704495061%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="tap-listener.html"><span>tap</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1704495061%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="tap-listener.html">tapListener</a><span class="token operator">: </span><a href="../-tap-listener/index.html">TapListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph"><a href="../-tap-listener/index.html">com.here.sdk.gestures.TapListener</a> that notifies when a tap gesture occurs.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1055059580%2FProperties%2F1617540583" anchor-label="twoFingerPanListener" id="1055059580%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="two-finger-pan-listener.html"><span>two</span><wbr></wbr><span>Finger</span><wbr></wbr><span>Pan</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1055059580%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="two-finger-pan-listener.html">twoFingerPanListener</a><span class="token operator">: </span><a href="../-two-finger-pan-listener/index.html">TwoFingerPanListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph"><a href="../-two-finger-pan-listener/index.html">com.here.sdk.gestures.TwoFingerPanListener</a> that notifies when a two-finger pan gesture occurs.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1977657290%2FProperties%2F1617540583" anchor-label="twoFingerTapListener" id="-1977657290%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="two-finger-tap-listener.html"><span>two</span><wbr></wbr><span>Finger</span><wbr></wbr><span>Tap</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1977657290%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="two-finger-tap-listener.html">twoFingerTapListener</a><span class="token operator">: </span><a href="../-two-finger-tap-listener/index.html">TwoFingerTapListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph"><a href="../-two-finger-tap-listener/index.html">com.here.sdk.gestures.TwoFingerTapListener</a> that notifies when a two-finger tap gesture occurs.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="-883483627%2FFunctions%2F1617540583" anchor-label="disableDefaultAction" id="-883483627%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="disable-default-action.html"><span>disable</span><wbr></wbr><span>Default</span><wbr></wbr><span><span>Action</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-883483627%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="disable-default-action.html"><span class="token function">disableDefaultAction</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">gestureType<span class="token operator">: </span><a href="../-gesture-type/index.html">GestureType</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Disables default action for a specified gesture.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-723504912%2FFunctions%2F1617540583" anchor-label="enableDefaultAction" id="-723504912%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="enable-default-action.html"><span>enable</span><wbr></wbr><span>Default</span><wbr></wbr><span><span>Action</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-723504912%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="enable-default-action.html"><span class="token function">enableDefaultAction</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">gestureType<span class="token operator">: </span><a href="../-gesture-type/index.html">GestureType</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Enables default action to be performed for a specified gesture.</p></div></div></div>
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
