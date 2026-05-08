---
title: "Companion"
slug: "sdk-for-flutter-explore"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>Companion</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.mapview/MapCameraKeyframeTrack.Companion///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.mapview</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">MapCameraKeyframeTrack</a><span class="delimiter">/</span><span class="current">Companion</span></div>
  <div class="cover ">
    <h1 class="cover"><span><span>Companion</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">object </span><a href="sdk-for-flutter-explore-index">Companion</a></div></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="-1308645970%2FFunctions%2F1617540583" anchor-label="fieldOfView" id="-1308645970%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-field-of-view"><span>field</span><wbr></wbr><span>Of</span><wbr></wbr><span><span>View</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1308645970%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-field-of-view"><span class="token function">fieldOfView</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">keyframes<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">ScalarKeyframe</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">easing<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Easing</a><span class="token punctuation">, </span></span><span class="parameter ">interpolationMode<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">KeyframeInterpolationMode</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraKeyframeTrack</a></div><div class="brief "><p class="paragraph">Creates a map camera field-of-view keyframe track. It enables animations over the angle of the field of view captured by the map camera in degrees. Values will be clamped to a range from 1 to 150.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1032539765%2FFunctions%2F1617540583" anchor-label="lookAtDistance" id="1032539765%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-look-at-distance"><span>look</span><wbr></wbr><span>At</span><wbr></wbr><span><span>Distance</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1032539765%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-look-at-distance"><span class="token function"><strike>lookAtDistance</strike></span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">keyframes<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">ScalarKeyframe</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">easing<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Easing</a><span class="token punctuation">, </span></span><span class="parameter ">interpolationMode<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">KeyframeInterpolationMode</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraKeyframeTrack</a></div><div class="brief "><p class="paragraph">Creates a map camera look-at distance keyframe track. It enables animations of the distance from the map camera to the target point that the camera looks at in meters. The values will be clamped according to the minimum and maximum zoom levels set for the map camera.</p></div><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-look-at-distance"><span class="token function">lookAtDistance</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">distanceKind<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMeasure.Kind</a><span class="token punctuation">, </span></span><span class="parameter ">keyframes<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">ScalarKeyframe</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">easing<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Easing</a><span class="token punctuation">, </span></span><span class="parameter ">interpolationMode<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">KeyframeInterpolationMode</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraKeyframeTrack</a></div><div class="brief "><p class="paragraph">Creates a map camera look-at distance keyframe track. It enables animations of the distance from the map camera to the target point that the camera looks at. The measure kind of that distance can be specified. The values will be clamped according to the minimum and maximum zoom levels set for the map camera.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1145902979%2FFunctions%2F1617540583" anchor-label="lookAtOrientation" id="1145902979%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-look-at-orientation"><span>look</span><wbr></wbr><span>At</span><wbr></wbr><span><span>Orientation</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1145902979%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-look-at-orientation"><span class="token function">lookAtOrientation</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">keyframes<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">GeoOrientationKeyframe</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">easing<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Easing</a><span class="token punctuation">, </span></span><span class="parameter ">interpolationMode<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">KeyframeInterpolationMode</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraKeyframeTrack</a></div><div class="brief "><p class="paragraph">Creates a map camera look-at orientation keyframe track. It enables animations over the orientation of the map camera target (bearing and tilt).</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-848407647%2FFunctions%2F1617540583" anchor-label="lookAtTarget" id="-848407647%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-look-at-target"><span>look</span><wbr></wbr><span>At</span><wbr></wbr><span><span>Target</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-848407647%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-look-at-target"><span class="token function">lookAtTarget</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">keyframes<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">GeoCoordinatesKeyframe</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">easing<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Easing</a><span class="token punctuation">, </span></span><span class="parameter ">interpolationMode<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">KeyframeInterpolationMode</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraKeyframeTrack</a></div><div class="brief "><p class="paragraph">Creates a map camera look-at target keyframe track. It enables animations over the geographical coordinates of the target point that the map camera is looking at. Altitude components of coordinates are ignored.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1777316518%2FFunctions%2F1617540583" anchor-label="normalizedPrincipalPoint" id="-1777316518%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-normalized-principal-point"><span>normalized</span><wbr></wbr><span>Principal</span><wbr></wbr><span><span>Point</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1777316518%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-normalized-principal-point"><span class="token function">normalizedPrincipalPoint</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">keyframes<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">Anchor2DKeyframe</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">easing<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Easing</a><span class="token punctuation">, </span></span><span class="parameter ">interpolationMode<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">KeyframeInterpolationMode</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraKeyframeTrack</a></div><div class="brief "><p class="paragraph">Creates a map camera principal point keyframe track. It enables animations on the point where the map camera's target is placed in normalized view coordinates. (0,0) is top left of the viewport, (1, 1) is bottom right.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="348847624%2FFunctions%2F1617540583" anchor-label="principalPoint" id="348847624%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-principal-point"><span>principal</span><wbr></wbr><span><span>Point</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="348847624%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-principal-point"><span class="token function">principalPoint</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">keyframes<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">Point2DKeyframe</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">easing<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Easing</a><span class="token punctuation">, </span></span><span class="parameter ">interpolationMode<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">KeyframeInterpolationMode</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraKeyframeTrack</a></div><div class="brief "><p class="paragraph">Creates a map camera principal point keyframe track. It enables animations on the pixel point where the map camera's target is placed in view coordinates. (0,0) is top left of the viewport, (viewport width, viewport height) is bottom right.</p></div></div></div>
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
