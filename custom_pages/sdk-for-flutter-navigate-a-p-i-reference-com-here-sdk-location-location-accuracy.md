---
title: "LocationAccuracy"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-location-location-accuracy"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>LocationAccuracy</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.location/LocationAccuracy///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.location</a><span class="delimiter">/</span><span class="current">LocationAccuracy</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Location</span><wbr></wbr><span><span>Accuracy</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="index.html">LocationAccuracy</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="index.html">LocationAccuracy</a><span class="token operator">&gt; </span></div><p class="paragraph">Indicates the desired location accuracy, however the actual accuracy is not guaranteed. When requesting high-accuracy locations, the initial update delivered by the LocationEngine may not have the requested accuracy. Requesting higher accuracy location updates usually means higher power consumption, therefore you should use the lowest accuracy suitable for your use case to preserve the device battery.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button><button class="section-tab" data-togglable="ENTRY">Entries</button></div>
    <div class="tabs-section-body">
      <div data-togglable="ENTRY">
        <h2 class="">Entries</h2>
        <div class="table"><a data-name="-461086515%2FClasslikes%2F1617540583" anchor-label="BEST_AVAILABLE" id="-461086515%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-b-e-s-t_-a-v-a-i-l-a-b-l-e/index.html">BEST_AVAILABLE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-461086515%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-b-e-s-t_-a-v-a-i-l-a-b-l-e/index.html">BEST_AVAILABLE</a></div></div><div class="brief "><p class="paragraph">The best accuracy available, using all possible sources: satellite, WiFi and Cell positioning. Additional sensor data may be used for improving positioning accuracy. Update frequency may vary between 1 second to about 30 seconds, so this is not the best option for navigation purposes, see <a href="-n-a-v-i-g-a-t-i-o-n/index.html">com.here.sdk.location.LocationAccuracy.NAVIGATION</a> and <a href="-s-u-b_-m-e-t-e-r_-n-a-v-i-g-a-t-i-o-n/index.html">com.here.sdk.location.LocationAccuracy.SUB_METER_NAVIGATION</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2076141016%2FClasslikes%2F1617540583" anchor-label="SUB_METER_NAVIGATION" id="-2076141016%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-u-b_-m-e-t-e-r_-n-a-v-i-g-a-t-i-o-n/index.html">SUB_METER_NAVIGATION</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2076141016%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-s-u-b_-m-e-t-e-r_-n-a-v-i-g-a-t-i-o-n/index.html">SUB_METER_NAVIGATION</a></div></div><div class="brief "><p class="paragraph">Decimeter accurate navigation using satellite and WiFi positioning. Additional sensor data may be used for improving positioning accuracy. Update frequency is as close to once per second as possible. This feature requires Android 12 or later and dual frequency GNSS receiver and raw GNSS measurements. This feature is disabled by default: <a href="https://www.here.com/platform/positioning">Contact us</a> to enable it. If it is not enabled or the OS/device requirements are not met, fallback to other positioning technologies may occur and desired accuracy level may not be reached.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1529755603%2FClasslikes%2F1617540583" anchor-label="NAVIGATION" id="1529755603%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-n-a-v-i-g-a-t-i-o-n/index.html">NAVIGATION</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1529755603%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-n-a-v-i-g-a-t-i-o-n/index.html">NAVIGATION</a></div></div><div class="brief "><p class="paragraph">The default accuracy when navigation is needed, using satellite and WiFi positioning. Additional sensor data is used for improving navigation accuracy. Update frequency is as close to once per second as possible.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="749563368%2FClasslikes%2F1617540583" anchor-label="TENS_OF_METERS" id="749563368%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-t-e-n-s_-o-f_-m-e-t-e-r-s/index.html">TENS_OF_METERS</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="749563368%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-t-e-n-s_-o-f_-m-e-t-e-r-s/index.html">TENS_OF_METERS</a></div></div><div class="brief "><p class="paragraph">Accurate to within tens of meters of the desired target. Additional sensor data may be used for improving localization accuracy.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-11913%2FClasslikes%2F1617540583" anchor-label="HUNDREDS_OF_METERS" id="-11913%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-h-u-n-d-r-e-d-s_-o-f_-m-e-t-e-r-s/index.html">HUNDREDS_OF_METERS</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-11913%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-h-u-n-d-r-e-d-s_-o-f_-m-e-t-e-r-s/index.html">HUNDREDS_OF_METERS</a></div></div><div class="brief "><p class="paragraph">Accurate to within hundreds of meters of the desired target.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1794134998%2FClasslikes%2F1617540583" anchor-label="KILOMETERS" id="-1794134998%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-k-i-l-o-m-e-t-e-r-s/index.html">KILOMETERS</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1794134998%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-k-i-l-o-m-e-t-e-r-s/index.html">KILOMETERS</a></div></div><div class="brief "><p class="paragraph">Accurate to within kilometers of the desired target.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="195332441%2FProperties%2F1617540583" anchor-label="entries" id="195332441%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="entries.html"><span><span>entries</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="195332441%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="entries.html">entries</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html">EnumEntries</a><span class="token operator">&lt;</span><a href="index.html">LocationAccuracy</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Returns a representation of an immutable list of all enum entries, in the order they're declared.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1438243176%2FProperties%2F1617540583" anchor-label="value" id="-1438243176%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="value.html"><span><span>value</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1438243176%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="value.html">value</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="866716899%2FFunctions%2F1617540583" anchor-label="valueOf" id="866716899%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="value-of.html"><span>value</span><wbr></wbr><span><span>Of</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="866716899%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><a href="value-of.html"><span class="token function">valueOf</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">value<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">LocationAccuracy</a></div><div class="brief "><p class="paragraph">Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-69610705%2FFunctions%2F1617540583" anchor-label="values" id="-69610705%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="values.html"><span><span>values</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-69610705%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><a href="values.html"><span class="token function">values</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="token operator">&lt;</span><a href="index.html">LocationAccuracy</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Returns an array containing the constants of this enum type, in the order they're declared.</p></div></div></div>
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
