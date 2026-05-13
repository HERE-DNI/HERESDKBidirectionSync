---
title: "PrivateBusBuilder"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-vehicle-specification-private-bus-builder"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>PrivateBusBuilder</title>
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
            <a class="library-name--link" href="../../../../index.html">
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.transport/VehicleSpecification.PrivateBusBuilder///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../../index.html">com.here.sdk.transport</a><span class="delimiter">/</span><a href="../index.html">VehicleSpecification</a><span class="delimiter">/</span><span class="current">PrivateBusBuilder</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Private</span><wbr></wbr><span>Bus</span><wbr></wbr><span><span>Builder</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">PrivateBusBuilder</a> : <a href="../../../com.here/-native-base/index.html">NativeBase</a></div><p class="paragraph">This class constructs a <a href="../index.html">com.here.sdk.transport.VehicleSpecification</a> for a private bus.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="670689564%2FConstructors%2F1617540583" anchor-label="PrivateBusBuilder" id="670689564%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-private-bus-builder.html"><span>Private</span><wbr></wbr><span>Bus</span><wbr></wbr><span><span>Builder</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="670689564%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of this class.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-864966559%2FClasslikes%2F1617540583" anchor-label="Companion" id="-864966559%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-864966559%2FClasslikes%2F1617540583"></span>
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
        <div class="table"><a data-name="-1072185620%2FFunctions%2F1617540583" anchor-label="build" id="-1072185620%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="build.html"><span><span>build</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1072185620%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="build.html"><span class="token function">build</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../index.html">VehicleSpecification</a></div><div class="brief "><p class="paragraph">Builds the <a href="../index.html">com.here.sdk.transport.VehicleSpecification</a> object for <a href="../../-transport-mode/-b-u-s/index.html">com.here.sdk.transport.TransportMode.BUS</a> with the specifications taken from the <a href="index.html">com.here.sdk.transport.VehicleSpecification.PrivateBusBuilder</a> object.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1430572607%2FFunctions%2F1617540583" anchor-label="withAxleCount" id="1430572607%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-axle-count.html"><span>with</span><wbr></wbr><span>Axle</span><wbr></wbr><span><span>Count</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1430572607%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-axle-count.html"><span class="token function">withAxleCount</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">axleCount<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">VehicleSpecification.PrivateBusBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle axle count.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-85888109%2FFunctions%2F1617540583" anchor-label="withCurrentWeightInKilograms" id="-85888109%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-current-weight-in-kilograms.html"><span>with</span><wbr></wbr><span>Current</span><wbr></wbr><span>Weight</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Kilograms</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-85888109%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-current-weight-in-kilograms.html"><span class="token function">withCurrentWeightInKilograms</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">currentWeightInKilograms<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">VehicleSpecification.PrivateBusBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle current weight in kilograms.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="440884391%2FFunctions%2F1617540583" anchor-label="withEmptyWeightInKilograms" id="440884391%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-empty-weight-in-kilograms.html"><span>with</span><wbr></wbr><span>Empty</span><wbr></wbr><span>Weight</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Kilograms</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="440884391%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-empty-weight-in-kilograms.html"><span class="token function">withEmptyWeightInKilograms</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">emptyWeightInKilograms<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">VehicleSpecification.PrivateBusBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle empty weight in kilograms.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="828787119%2FFunctions%2F1617540583" anchor-label="withEngineSizeInCubicCentimeters" id="828787119%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-engine-size-in-cubic-centimeters.html"><span>with</span><wbr></wbr><span>Engine</span><wbr></wbr><span>Size</span><wbr></wbr><span>In</span><wbr></wbr><span>Cubic</span><wbr></wbr><span><span>Centimeters</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="828787119%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-engine-size-in-cubic-centimeters.html"><span class="token function">withEngineSizeInCubicCentimeters</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">engineSizeInCubicCentimeters<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">VehicleSpecification.PrivateBusBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle engine size in cubic centimeters.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-659615714%2FFunctions%2F1617540583" anchor-label="withGrossWeightInKilograms" id="-659615714%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-gross-weight-in-kilograms.html"><span>with</span><wbr></wbr><span>Gross</span><wbr></wbr><span>Weight</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Kilograms</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-659615714%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-gross-weight-in-kilograms.html"><span class="token function">withGrossWeightInKilograms</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">grossWeightInKilograms<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">VehicleSpecification.PrivateBusBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle gross weight in kilograms.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-292345665%2FFunctions%2F1617540583" anchor-label="withHeightInCentimeters" id="-292345665%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-height-in-centimeters.html"><span>with</span><wbr></wbr><span>Height</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Centimeters</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-292345665%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-height-in-centimeters.html"><span class="token function">withHeightInCentimeters</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">heightInCentimeters<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">VehicleSpecification.PrivateBusBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle height in centimeters.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1669286859%2FFunctions%2F1617540583" anchor-label="withIsCommercial" id="1669286859%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-is-commercial.html"><span>with</span><wbr></wbr><span>Is</span><wbr></wbr><span><span>Commercial</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1669286859%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-is-commercial.html"><span class="token function">withIsCommercial</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">isCommercial<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">VehicleSpecification.PrivateBusBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle is commercial flag.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-143503517%2FFunctions%2F1617540583" anchor-label="withLastCharacterOfLicensePlate" id="-143503517%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-last-character-of-license-plate.html"><span>with</span><wbr></wbr><span>Last</span><wbr></wbr><span>Character</span><wbr></wbr><span>Of</span><wbr></wbr><span>License</span><wbr></wbr><span><span>Plate</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-143503517%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-last-character-of-license-plate.html"><span class="token function">withLastCharacterOfLicensePlate</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">lastCharacterOfLicensePlate<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">VehicleSpecification.PrivateBusBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle last character of the license plate.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1782794114%2FFunctions%2F1617540583" anchor-label="withLengthInCentimeters" id="-1782794114%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-length-in-centimeters.html"><span>with</span><wbr></wbr><span>Length</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Centimeters</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1782794114%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-length-in-centimeters.html"><span class="token function">withLengthInCentimeters</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">lengthInCentimeters<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">VehicleSpecification.PrivateBusBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle length in centimeters.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-851322319%2FFunctions%2F1617540583" anchor-label="withOccupancy" id="-851322319%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-occupancy.html"><span>with</span><wbr></wbr><span><span>Occupancy</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-851322319%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-occupancy.html"><span class="token function">withOccupancy</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">occupancy<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">VehicleSpecification.PrivateBusBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle occupants number.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="148412596%2FFunctions%2F1617540583" anchor-label="withTiresCount" id="148412596%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-tires-count.html"><span>with</span><wbr></wbr><span>Tires</span><wbr></wbr><span><span>Count</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="148412596%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-tires-count.html"><span class="token function">withTiresCount</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">tiresCount<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">VehicleSpecification.PrivateBusBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle tires count.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="466840748%2FFunctions%2F1617540583" anchor-label="withTrailerAxleCount" id="466840748%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-trailer-axle-count.html"><span>with</span><wbr></wbr><span>Trailer</span><wbr></wbr><span>Axle</span><wbr></wbr><span><span>Count</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="466840748%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-trailer-axle-count.html"><span class="token function">withTrailerAxleCount</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">trailerAxleCount<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">VehicleSpecification.PrivateBusBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle trailer axle count.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1160988828%2FFunctions%2F1617540583" anchor-label="withTrailerCount" id="1160988828%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-trailer-count.html"><span>with</span><wbr></wbr><span>Trailer</span><wbr></wbr><span><span>Count</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1160988828%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-trailer-count.html"><span class="token function">withTrailerCount</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">trailerCount<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">VehicleSpecification.PrivateBusBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle trailer count.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-685354210%2FFunctions%2F1617540583" anchor-label="withTunnelCategory" id="-685354210%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-tunnel-category.html"><span>with</span><wbr></wbr><span>Tunnel</span><wbr></wbr><span><span>Category</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-685354210%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-tunnel-category.html"><span class="token function">withTunnelCategory</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">tunnelCategory<span class="token operator">: </span><a href="../../-tunnel-category/index.html">TunnelCategory</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">VehicleSpecification.PrivateBusBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle tunnel category.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1165742434%2FFunctions%2F1617540583" anchor-label="withWeightPerAxleGroup" id="-1165742434%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-weight-per-axle-group.html"><span>with</span><wbr></wbr><span>Weight</span><wbr></wbr><span>Per</span><wbr></wbr><span>Axle</span><wbr></wbr><span><span>Group</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1165742434%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-weight-per-axle-group.html"><span class="token function">withWeightPerAxleGroup</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">weightPerAxleGroup<span class="token operator">: </span><a href="../../-weight-per-axle-group/index.html">WeightPerAxleGroup</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">VehicleSpecification.PrivateBusBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle weight per axle group.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2119719849%2FFunctions%2F1617540583" anchor-label="withWeightPerAxleInKilograms" id="-2119719849%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-weight-per-axle-in-kilograms.html"><span>with</span><wbr></wbr><span>Weight</span><wbr></wbr><span>Per</span><wbr></wbr><span>Axle</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Kilograms</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2119719849%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-weight-per-axle-in-kilograms.html"><span class="token function">withWeightPerAxleInKilograms</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">weightPerAxleInKilograms<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">VehicleSpecification.PrivateBusBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle weight per axle in kilograms.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="527947128%2FFunctions%2F1617540583" anchor-label="withWidthInCentimeters" id="527947128%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-width-in-centimeters.html"><span>with</span><wbr></wbr><span>Width</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Centimeters</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="527947128%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-width-in-centimeters.html"><span class="token function">withWidthInCentimeters</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">widthInCentimeters<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">VehicleSpecification.PrivateBusBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle width in centimeters.</p></div></div></div>
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
