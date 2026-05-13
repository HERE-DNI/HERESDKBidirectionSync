---
title: "com.here.sdk.gestures"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-gestures"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>com.here.sdk.gestures</title>
    <link href="../../images/logo-icon.svg" rel="icon" type="image/svg">
    <script>var pathToRoot = "../../";</script>
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
<script type="text/javascript" src="../../scripts/sourceset_dependencies.js" async="async"></script>
<link href="../../styles/style.css" rel="Stylesheet">
<link href="../../styles/main.css" rel="Stylesheet">
<link href="../../styles/prism.css" rel="Stylesheet">
<link href="../../styles/logo-styles.css" rel="Stylesheet">
<link href="../../styles/font-jb-sans-auto.css" rel="Stylesheet">
<link href="../../ui-kit/ui-kit.min.css" rel="Stylesheet">
<script type="text/javascript" src="../../scripts/clipboard.js" async="async"></script>
<script type="text/javascript" src="../../scripts/navigation-loader.js" async="async"></script>
<script type="text/javascript" src="../../scripts/platform-content-handler.js" async="async"></script>
<script type="text/javascript" src="../../scripts/main.js" defer="defer"></script>
<script type="text/javascript" src="../../scripts/prism.js" async="async"></script>
<script type="text/javascript" src="../../ui-kit/ui-kit.min.js" defer="defer"></script>
<script type="text/javascript" src="../../scripts/symbol-parameters-wrapper_deferred.js" defer="defer"></script>
</head>
<body>
    <div class="root">
    <nav class="navigation theme-dark" id="navigation-wrapper">
            <a class="library-name--link" href="../../index.html">
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
<div class="main-content" data-page-type="package" id="content" pageIds="API Reference::com.here.sdk.gestures////PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../index.html">API Reference</a><span class="delimiter">/</span><span class="current">com.here.sdk.gestures</span></div>
  <div class="cover ">
    <h1 class="cover"><span><span>Package-level</span></span> <span><span>declarations</span></span></h1>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="TYPE">Types</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="430703787%2FClasslikes%2F1617540583" anchor-label="DoubleTapListener" id="430703787%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-double-tap-listener/index.html"><span>Double</span><wbr></wbr><span>Tap</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="430703787%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-double-tap-listener/index.html">DoubleTapListener</a></div><div class="brief "><p class="paragraph">Interface for handling double tap gestures. Double-tap gesture occurs after double-tapping on the screen.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1652310269%2FClasslikes%2F1617540583" anchor-label="FlingHandler" id="-1652310269%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-fling-handler/index.html"><span>Fling</span><wbr></wbr><span><span>Handler</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1652310269%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-fling-handler/index.html">FlingHandler</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">This class handles fling events by performing a kinetic move on the map. Initial velocity of kinetic move is the one provided to <a href="-fling-handler/on-fling.html">com.here.sdk.gestures.FlingHandler.onFling</a>. Subsequently, velocity decays exponentially.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-765560697%2FClasslikes%2F1617540583" anchor-label="Gestures" id="-765560697%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-gestures/index.html"><span><span>Gestures</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-765560697%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-gestures/index.html">Gestures</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Use this class to process touch events from the platform and detect gesture induced actions on the map view. Please note that this class holds strong references to the gesture listeners. On Android Auto, processing touch events is not needed. Instead, gestures get detected by android auto platform and provided via callbacks. For more information see onClick, onFling and onScale methods in <a href="https://developer.android.com/reference/androidx/car/app/SurfaceCallback">https://developer.android.com/reference/androidx/car/app/SurfaceCallback</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-242966071%2FClasslikes%2F1617540583" anchor-label="GestureState" id="-242966071%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-gesture-state/index.html"><span>Gesture</span><wbr></wbr><span><span>State</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-242966071%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-gesture-state/index.html">GestureState</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-gesture-state/index.html">GestureState</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Represents the state of the gesture.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-51971058%2FClasslikes%2F1617540583" anchor-label="GestureType" id="-51971058%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-gesture-type/index.html"><span>Gesture</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-51971058%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-gesture-type/index.html">GestureType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-gesture-type/index.html">GestureType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Enum that represents the type of a gesture.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2044718943%2FClasslikes%2F1617540583" anchor-label="InternalGestureDetector" id="2044718943%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-internal-gesture-detector/index.html"><span>Internal</span><wbr></wbr><span>Gesture</span><wbr></wbr><span><span>Detector</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2044718943%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-internal-gesture-detector/index.html">InternalGestureDetector</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-447410634%2FClasslikes%2F1617540583" anchor-label="LongPressListener" id="-447410634%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-long-press-listener/index.html"><span>Long</span><wbr></wbr><span>Press</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-447410634%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-long-press-listener/index.html">LongPressListener</a></div><div class="brief "><p class="paragraph">Interface for handling long-press gestures. Long-press gesture occurs after tapping and holding the finger for a long time on the screen.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1611462528%2FClasslikes%2F1617540583" anchor-label="PanListener" id="1611462528%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-pan-listener/index.html"><span>Pan</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1611462528%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-pan-listener/index.html">PanListener</a></div><div class="brief "><p class="paragraph">Interface for handling pan gestures. Pan gesture occurs when a finger is moving on the screen.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-620550040%2FClasslikes%2F1617540583" anchor-label="PinchRotateListener" id="-620550040%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-pinch-rotate-listener/index.html"><span>Pinch</span><wbr></wbr><span>Rotate</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-620550040%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-pinch-rotate-listener/index.html">PinchRotateListener</a></div><div class="brief "><p class="paragraph">Interface for handling pinch rotate gestures. Pinch rotate gesture occurs when two fingers are on the screen and at least one of them moves.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-635731215%2FClasslikes%2F1617540583" anchor-label="ScaleHandler" id="-635731215%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-scale-handler/index.html"><span>Scale</span><wbr></wbr><span><span>Handler</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-635731215%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-scale-handler/index.html">ScaleHandler</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">This class handles scale events by zooming the map accordingly.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1175973452%2FClasslikes%2F1617540583" anchor-label="ScrollHandler" id="-1175973452%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-scroll-handler/index.html"><span>Scroll</span><wbr></wbr><span><span>Handler</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1175973452%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-scroll-handler/index.html">ScrollHandler</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">This class handles scroll events by panning the map accordingly.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1421254342%2FClasslikes%2F1617540583" anchor-label="TapListener" id="-1421254342%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-tap-listener/index.html"><span>Tap</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1421254342%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-tap-listener/index.html">TapListener</a></div><div class="brief "><p class="paragraph">Interface for handling tap gestures. Tap gesture occurs after tapping on the screen.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1386567499%2FClasslikes%2F1617540583" anchor-label="TwoFingerPanListener" id="-1386567499%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-two-finger-pan-listener/index.html"><span>Two</span><wbr></wbr><span>Finger</span><wbr></wbr><span>Pan</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1386567499%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-two-finger-pan-listener/index.html">TwoFingerPanListener</a></div><div class="brief "><p class="paragraph">Interface for handling two finger pan gestures. Two finger pan gesture occurs when two fingers are on the screen and both of them are moving vertically.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-124317073%2FClasslikes%2F1617540583" anchor-label="TwoFingerTapListener" id="-124317073%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-two-finger-tap-listener/index.html"><span>Two</span><wbr></wbr><span>Finger</span><wbr></wbr><span>Tap</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-124317073%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-two-finger-tap-listener/index.html">TwoFingerTapListener</a></div><div class="brief "><p class="paragraph">Interface for handling two finger tap gestures. Two finger tap gesture occurs after tapping on the screen with two fingers.</p></div></div></div>
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
