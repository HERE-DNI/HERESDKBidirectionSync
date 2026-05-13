---
title: "ManeuverNotificationOptions"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-navigation-maneuver-notification-options"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>ManeuverNotificationOptions</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.navigation/ManeuverNotificationOptions///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.navigation</a><span class="delimiter">/</span><span class="current">ManeuverNotificationOptions</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Maneuver</span><wbr></wbr><span>Notification</span><wbr></wbr><span><span>Options</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">ManeuverNotificationOptions</a></div><p class="paragraph">A class containing all options to be used when generating maneuver notifications.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="-86618193%2FConstructors%2F1617540583" anchor-label="ManeuverNotificationOptions" id="-86618193%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-maneuver-notification-options.html"><span>Maneuver</span><wbr></wbr><span>Notification</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-86618193%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of this class with default configurations.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">language<span class="token operator">: </span><a href="../../com.here.sdk.core/-language-code/index.html">LanguageCode</a><span class="token punctuation">, </span></span><span class="parameter ">unitSystem<span class="token operator">: </span><a href="../../com.here.sdk.core/-unit-system/index.html">UnitSystem</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of this class with specified language and unit system.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">language<span class="token operator">: </span><a href="../../com.here.sdk.core/-language-code/index.html">LanguageCode</a><span class="token punctuation">, </span></span><span class="parameter ">unitSystem<span class="token operator">: </span><a href="../../com.here.sdk.core/-unit-system/index.html">UnitSystem</a><span class="token punctuation">, </span></span><span class="parameter ">includedNotificationTypes<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="../-maneuver-notification-type/index.html">ManeuverNotificationType</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">enableRoundaboutNotification<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="token punctuation">, </span></span><span class="parameter ">enableDestinationReachedNotification<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="token punctuation">, </span></span><span class="parameter ">enableDoubleNotification<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="token punctuation">, </span></span><span class="parameter ">enablePhoneme<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="token punctuation">, </span></span><span class="parameter ">textUsageOptions<span class="token operator">: </span><a href="../../com.here.sdk.routing/-text-usage-options/index.html">TextUsageOptions</a><span class="token punctuation">, </span></span><span class="parameter ">enableHighwayExit<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of this class with full specified configurations.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">language<span class="token operator">: </span><a href="../../com.here.sdk.core/-language-code/index.html">LanguageCode</a><span class="token punctuation">, </span></span><span class="parameter ">unitSystem<span class="token operator">: </span><a href="../../com.here.sdk.core/-unit-system/index.html">UnitSystem</a><span class="token punctuation">, </span></span><span class="parameter ">includedNotificationTypes<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="../-maneuver-notification-type/index.html">ManeuverNotificationType</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">enableRoundaboutNotification<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="token punctuation">, </span></span><span class="parameter ">enableDestinationReachedNotification<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="token punctuation">, </span></span><span class="parameter ">enableDoubleNotification<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="token punctuation">, </span></span><span class="parameter ">enablePhoneme<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="token punctuation">, </span></span><span class="parameter ">enableHighwayExit<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of this class with full specified configurations.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">language<span class="token operator">: </span><a href="../../com.here.sdk.core/-language-code/index.html">LanguageCode</a><span class="token punctuation">, </span></span><span class="parameter ">unitSystem<span class="token operator">: </span><a href="../../com.here.sdk.core/-unit-system/index.html">UnitSystem</a><span class="token punctuation">, </span></span><span class="parameter ">includedNotificationTypes<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="../-maneuver-notification-type/index.html">ManeuverNotificationType</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">enableRoundaboutNotification<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="token punctuation">, </span></span><span class="parameter ">enableDestinationReachedNotification<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="token punctuation">, </span></span><span class="parameter ">enableDoubleNotification<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="token punctuation">, </span></span><span class="parameter ">enablePhoneme<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="token punctuation">, </span></span><span class="parameter ">notificationFormatOption<span class="token operator">: </span><a href="../-notification-format-option/index.html">NotificationFormatOption</a><span class="token punctuation">, </span></span><span class="parameter ">enableHighwayExit<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of this class with full specified configurations.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="399087919%2FProperties%2F1617540583" anchor-label="arrivalNotificationOption" id="399087919%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="arrival-notification-option.html"><span>arrival</span><wbr></wbr><span>Notification</span><wbr></wbr><span><span>Option</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="399087919%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="arrival-notification-option.html">arrivalNotificationOption</a><span class="token operator">: </span><a href="../-arrival-notification-option/index.html">ArrivalNotificationOption</a></div><div class="brief "><p class="paragraph">A flag that indicates whether notification for destination and/or stopover reached maneuvers should be generated. Defaults to <code class="lang-kotlin">ArrivalNotificationOption.BOTH</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-556860185%2FProperties%2F1617540583" anchor-label="directionInformationUsageForActionNotificationOption" id="-556860185%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="direction-information-usage-for-action-notification-option.html"><span>direction</span><wbr></wbr><span>Information</span><wbr></wbr><span>Usage</span><wbr></wbr><span>For</span><wbr></wbr><span>Action</span><wbr></wbr><span>Notification</span><wbr></wbr><span><span>Option</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-556860185%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="direction-information-usage-for-action-notification-option.html">directionInformationUsageForActionNotificationOption</a><span class="token operator">: </span><a href="../-direction-information-usage-option/index.html">DirectionInformationUsageOption</a></div><div class="brief "><p class="paragraph">An option whether direction information should be used when generating notification with <a href="../-maneuver-notification-type/-a-c-t-i-o-n/index.html">com.here.sdk.navigation.ManeuverNotificationType.ACTION</a>. Defaults to <a href="../-direction-information-usage-option/-n-o-n-e/index.html">com.here.sdk.navigation.DirectionInformationUsageOption.NONE</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1820346400%2FProperties%2F1617540583" anchor-label="enableDestinationReachedNotification" id="-1820346400%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="enable-destination-reached-notification.html"><span>enable</span><wbr></wbr><span>Destination</span><wbr></wbr><span>Reached</span><wbr></wbr><span><span>Notification</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1820346400%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="enable-destination-reached-notification.html"><strike>enableDestinationReachedNotification</strike></a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">A flag that indicates whether notification for destination/stopover reached maneuvers should be generated. Defaults to <code class="lang-kotlin">true</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1557347181%2FProperties%2F1617540583" anchor-label="enableDoubleNotification" id="-1557347181%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="enable-double-notification.html"><span>enable</span><wbr></wbr><span>Double</span><wbr></wbr><span><span>Notification</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1557347181%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="enable-double-notification.html">enableDoubleNotification</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">A flag that indicates whether combined maneuver notifications should be generated. Such double notifications can be useful when maneuvers are very close. <strong>Example:</strong> A combined message: 'After 300 meters turn left and then turn right.'. This way a user can better anticipate the next-next maneuver. Note that setting to <code class="lang-kotlin">true</code> will make the notification longer as two maneuvers will be merged into one. When the next-next maneuver action takes place, the notification will be given as usual. <strong>Example:</strong> 'Now turn left and then then turn right.' will be followed by 'Now turn right.'. Defaults to <code class="lang-kotlin">true</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-107628320%2FProperties%2F1617540583" anchor-label="enableHighwayExit" id="-107628320%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="enable-highway-exit.html"><span>enable</span><wbr></wbr><span>Highway</span><wbr></wbr><span><span>Exit</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-107628320%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="enable-highway-exit.html">enableHighwayExit</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">A flag that indicates whether highway exit information should be used when generating notification. Defaults to <code class="lang-kotlin">true</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="703025994%2FProperties%2F1617540583" anchor-label="enableLaneRecommendation" id="703025994%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="enable-lane-recommendation.html"><span>enable</span><wbr></wbr><span>Lane</span><wbr></wbr><span><span>Recommendation</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="703025994%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="enable-lane-recommendation.html">enableLaneRecommendation</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">A flag that indicates whether lane recommendation should be used when generating notifications. In case the flag is enabled, <i>only</i> the notification for the <a href="../-maneuver-notification-type/-d-i-s-t-a-n-c-e/index.html">com.here.sdk.navigation.ManeuverNotificationType.DISTANCE</a> maneuver notification type will contain the lane recommendation. The lane recommandation will replace the direction information in the notification. <strong>Example:</strong> 'After 250 meters use the right two lanes and turn right.'. Defaults to <code class="lang-kotlin">false</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1926671995%2FProperties%2F1617540583" anchor-label="enablePhoneme" id="-1926671995%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="enable-phoneme.html"><span>enable</span><wbr></wbr><span><span>Phoneme</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1926671995%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="enable-phoneme.html">enablePhoneme</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">A flag that indicates whether phonemes in selected notification format for proper nouns (e.g. road names, road numbers, city names) should be used when generating notifications. Direction information comes usually in orthographic form and phoneme (e.g. Wall Street and &quot;wɔːl&quot;striːt). However, when the notification is synthesized by a TTS engine, the pronunciation of the orthographic form solely depends on its capability and phoneme set. The use of our phoneme data in the notification usually makes the pronunciation of direction information sound more natural. <strong>Note:</strong> For now, this property is functional for road name and road number information only.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-659048091%2FProperties%2F1617540583" anchor-label="enableRoundaboutNotification" id="-659048091%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="enable-roundabout-notification.html"><span>enable</span><wbr></wbr><span>Roundabout</span><wbr></wbr><span><span>Notification</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-659048091%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="enable-roundabout-notification.html">enableRoundaboutNotification</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">A flag that indicates whether notification for roundabout-related maneuvers should be generated. Defaults to <code class="lang-kotlin">true</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-768358210%2FProperties%2F1617540583" anchor-label="includedNaturalGuidanceTypes" id="-768358210%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="included-natural-guidance-types.html"><span>included</span><wbr></wbr><span>Natural</span><wbr></wbr><span>Guidance</span><wbr></wbr><span><span>Types</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-768358210%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="included-natural-guidance-types.html">includedNaturalGuidanceTypes</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="../-natural-guidance-type/index.html">NaturalGuidanceType</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">List of <a href="../-natural-guidance-type/index.html">com.here.sdk.navigation.NaturalGuidanceType</a> should be included in the notifications. Excluding all of them will disable natural guidance information in the notifications completely.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-205980810%2FProperties%2F1617540583" anchor-label="includedNotificationTypes" id="-205980810%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="included-notification-types.html"><span>included</span><wbr></wbr><span>Notification</span><wbr></wbr><span><span>Types</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-205980810%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="included-notification-types.html">includedNotificationTypes</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="../-maneuver-notification-type/index.html">ManeuverNotificationType</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">List of <a href="../-maneuver-notification-type/index.html">com.here.sdk.navigation.ManeuverNotificationType</a> for which notifications should be generated. Excluding all of them will disable the maneuver notifications completely. By default, all types are included.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1090074726%2FProperties%2F1617540583" anchor-label="language" id="-1090074726%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="language.html"><span><span>language</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1090074726%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="language.html">language</a><span class="token operator">: </span><a href="../../com.here.sdk.core/-language-code/index.html">LanguageCode</a></div><div class="brief "><p class="paragraph">The language in which the notifications will be generated. When the specified language is not supported, the default language is used, which is English (American).</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1558798843%2FProperties%2F1617540583" anchor-label="notificationFormatOption" id="1558798843%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="notification-format-option.html"><span>notification</span><wbr></wbr><span>Format</span><wbr></wbr><span><span>Option</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1558798843%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="notification-format-option.html">notificationFormatOption</a><span class="token operator">: </span><a href="../-notification-format-option/index.html">NotificationFormatOption</a></div><div class="brief "><p class="paragraph">A formatting option for the phoneme that is included in the notification. By default, no phoneme is used and the <a href="../-notification-format-option/-p-l-a-i-n/index.html">com.here.sdk.navigation.NotificationFormatOption.PLAIN</a> orthographic form is included in the notification.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1030645080%2FProperties%2F1617540583" anchor-label="textUsageOptions" id="-1030645080%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="text-usage-options.html"><span>text</span><wbr></wbr><span>Usage</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1030645080%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="text-usage-options.html">textUsageOptions</a><span class="token operator">: </span><a href="../../com.here.sdk.routing/-text-usage-options/index.html">TextUsageOptions</a></div><div class="brief "><p class="paragraph">An option whether street name, road number and sign post direction should be used when generating notification. Defaults to each attribute as <a href="../../com.here.sdk.routing/-localized-text-preference/-u-s-e_-a-l-w-a-y-s/index.html">com.here.sdk.routing.LocalizedTextPreference.USE_ALWAYS</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="420293951%2FProperties%2F1617540583" anchor-label="unitSystem" id="420293951%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="unit-system.html"><span>unit</span><wbr></wbr><span><span>System</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="420293951%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="unit-system.html">unitSystem</a><span class="token operator">: </span><a href="../../com.here.sdk.core/-unit-system/index.html">UnitSystem</a></div><div class="brief "><p class="paragraph">Defines the measurement system used for distances. Defaults to metric.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="-1370369073%2FFunctions%2F1617540583" anchor-label="equals" id="-1370369073%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="equals.html"><span><span>equals</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1370369073%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">operator override </span><span class="token keyword">fun </span><a href="equals.html"><span class="token function">equals</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">other<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="token operator">?</span></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1631518665%2FFunctions%2F1617540583" anchor-label="hashCode" id="-1631518665%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="hash-code.html"><span>hash</span><wbr></wbr><span><span>Code</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1631518665%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">fun </span><a href="hash-code.html"><span class="token function">hashCode</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
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
