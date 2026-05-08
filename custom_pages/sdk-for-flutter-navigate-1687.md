---
title: "ManeuverNotificationTimingOptions"
slug: "sdk-for-flutter-navigate"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>ManeuverNotificationTimingOptions</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.navigation/ManeuverNotificationTimingOptions///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.navigation</a><span class="delimiter">/</span><span class="current">ManeuverNotificationTimingOptions</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Maneuver</span><wbr></wbr><span>Notification</span><wbr></wbr><span>Timing</span><wbr></wbr><span><span>Options</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">ManeuverNotificationTimingOptions</a></div><p class="paragraph">A class defining timing and distance thresholds for maneuver notifications.</p><p class="paragraph">Setting custom values will impact the time when the notification for each supported <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.ManeuverNotificationType</a> is sent - dependent on the <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.TimingProfile</a>.</p><p class="paragraph"><strong>Note:</strong> By default, notification thresholds depend on <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.TimingProfile</a>. When custom values are set, then these rules will still apply. The following rules apply for all transport modes:</p><ul><li><p class="paragraph">For <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.TimingProfile.FAST_SPEED</a> timing profile, if the current speed limit is less than 62 m/h (100 km/h), then the notification thresholds for <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.TimingProfile.REGULAR_SPEED</a> timing profile will be used instead.</p></li><li><p class="paragraph">For <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.TimingProfile.REGULAR_SPEED</a> timing profile, if the current speed limit is less than 37 m/h (60 km/h), then the notification thresholds for <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.TimingProfile.SLOW_SPEED</a> timing profile will be used instead.</p></li><li><p class="paragraph">For <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.TimingProfile.SLOW_SPEED</a> timing profile the thresholds will be always used as specified.</p></li></ul><p class="paragraph">The timings follow a strict order:</p><ol><li><p class="paragraph"><a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.ManeuverNotificationType.RANGE</a>: The first notification, it may be very far away (use 0 for farthest or earliest possible notification).</p></li><li><p class="paragraph"><a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.ManeuverNotificationType.REMINDER</a>: The second notification.</p></li><li><p class="paragraph"><a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.ManeuverNotificationType.DISTANCE</a>: A second reminder notification to take action.</p></li><li><p class="paragraph"><a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.ManeuverNotificationType.ACTION</a>: Final notification, specifying the required action to be taken.</p></li></ol><p class="paragraph">Therefore, it is crucial that the set values do not violate the order: range reminder distance action. For example, the following values are valid: range = 4000, reminder = 2500, distance = 1000, action = 400. If <a href="sdk-for-flutter-explore-range-notification-distance-in-meters">com.here.sdk.navigation.ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters</a> is smaller than <a href="sdk-for-flutter-explore-reminder-notification-distance-in-meters">com.here.sdk.navigation.ManeuverNotificationTimingOptions.reminderNotificationDistanceInMeters</a> the new options will be silently ignored and the previous values are kept.</p><p class="paragraph">You always have the choice to specify the thresholds for time or distance. For each <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.ManeuverNotificationType</a> a notification is only sent once, so the value that is reached first, wins. However, it is recommended to always update both, time and distance values. A configuration value of 0 is only allowed for <a href="sdk-for-flutter-explore-range-notification-distance-in-meters">com.here.sdk.navigation.ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters</a> and <a href="sdk-for-flutter-explore-range-notification-time-in-seconds">com.here.sdk.navigation.ManeuverNotificationTimingOptions.rangeNotificationTimeInSeconds</a>. It means that the maneuver notifications of type <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.ManeuverNotificationType.RANGE</a> should be generated as soon as the maneuver location is known - no matter how far away it may be. It's impossible for the other types to have 0 as value due to the descending ordering rule mentioned above.</p><p class="paragraph">You can also specify the <a href="sdk-for-flutter-explore-double-notification-distance-in-meters">com.here.sdk.navigation.ManeuverNotificationTimingOptions.doubleNotificationDistanceInMeters</a> threshold that determines the distance between two maneuvers that should be merged into a single maneuver notification, for example, when they are very close to each other. Maneuvers below this threshold will be merged like in this example: &quot;After 300 meters turn right and then turn left.&quot;.</p><p class="paragraph">Tip: To set the timings to the HERE SDK, you can first call <code class="lang-kotlin">getManeuverNotificationTimingOptions()</code> to get the default values for the desired combination of transport mode and timing profile. Then configure the timings, then set it back by calling the <code class="lang-kotlin">setManeuverNotificationTimingOptions()</code>.</p><p class="paragraph">Note: In the comment of each attribute, the term <code class="lang-kotlin">Others</code> refers to non-pedestrian transport modes such as <a href="sdk-for-flutter-explore-index">com.here.sdk.transport.TransportMode.CAR</a>, <a href="sdk-for-flutter-explore-index">com.here.sdk.transport.TransportMode.BICYCLE</a>, <a href="sdk-for-flutter-explore-index">com.here.sdk.transport.TransportMode.TRUCK</a>.</p><p class="paragraph">Attention: The default values for <a href="sdk-for-flutter-explore-index">com.here.sdk.transport.TransportMode.PEDESTRIAN</a> on <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.TimingProfile.FAST_SPEED</a> are theoretical, as such routes cannot be calculated with the HERE SDK as highways are forbidden for pedestrians.</p><p class="paragraph">Usage example:</p><div class="sample-container"><pre><code class="block lang-kotlin" theme="idea">// Get current values or default values, if no values have been set before.<br>ManeuverNotificationTimingOptions car_highway_timings = Navigator.getManeuverNotificationTimingOptions(TransportMode.CAR, TimingProfile.FAST_SPEED);<br>// Set a new value for a specific option and keep the previous or default values for the others.<br>car_highway_timings.distanceNotificationDistanceInMeters = 1500;<br>// Apply the changes to Navigator (or VisualNavigator).<br>Navigator.setManeuverNotificationTimingOptions(TransportMode.CAR, TimingProfile.FAST_SPEED, car_fast_speed_timings);</code></pre><span class="top-right-position"><span class="copy-icon"></span><div class="copy-popup-wrapper popup-to-left"><span class="copy-popup-icon"></span><span>Content copied to clipboard</span></div></span></div></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="1711356512%2FConstructors%2F1617540583" anchor-label="ManeuverNotificationTimingOptions" id="1711356512%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-maneuver-notification-timing-options"><span>Maneuver</span><wbr></wbr><span>Notification</span><wbr></wbr><span>Timing</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1711356512%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">rangeNotificationDistanceInMeters<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token punctuation">, </span></span><span class="parameter ">rangeNotificationTimeInSeconds<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token punctuation">, </span></span><span class="parameter ">reminderNotificationDistanceInMeters<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token punctuation">, </span></span><span class="parameter ">reminderNotificationTimeInSeconds<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token punctuation">, </span></span><span class="parameter ">distanceNotificationDistanceInMeters<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token punctuation">, </span></span><span class="parameter ">distanceNotificationTimeInSeconds<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token punctuation">, </span></span><span class="parameter ">actionNotificationDistanceInMeters<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token punctuation">, </span></span><span class="parameter ">actionNotificationTimeInSeconds<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token punctuation">, </span></span><span class="parameter ">doubleNotificationDistanceInMeters<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="-2014982365%2FProperties%2F1617540583" anchor-label="actionNotificationDistanceInMeters" id="-2014982365%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-action-notification-distance-in-meters"><span>action</span><wbr></wbr><span>Notification</span><wbr></wbr><span>Distance</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Meters</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2014982365%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-action-notification-distance-in-meters">actionNotificationDistanceInMeters</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief "><p class="paragraph">The default distance setting for <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.ManeuverNotificationType.ACTION</a> notification.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-882932282%2FProperties%2F1617540583" anchor-label="actionNotificationTimeInSeconds" id="-882932282%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-action-notification-time-in-seconds"><span>action</span><wbr></wbr><span>Notification</span><wbr></wbr><span>Time</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Seconds</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-882932282%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-action-notification-time-in-seconds">actionNotificationTimeInSeconds</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief "><p class="paragraph">The default time setting for <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.ManeuverNotificationType.ACTION</a> notification.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-131083260%2FProperties%2F1617540583" anchor-label="distanceNotificationDistanceInMeters" id="-131083260%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-distance-notification-distance-in-meters"><span>distance</span><wbr></wbr><span>Notification</span><wbr></wbr><span>Distance</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Meters</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-131083260%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-distance-notification-distance-in-meters">distanceNotificationDistanceInMeters</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief "><p class="paragraph">The default distance setting for <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.ManeuverNotificationType.DISTANCE</a> notification.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1182165883%2FProperties%2F1617540583" anchor-label="distanceNotificationTimeInSeconds" id="-1182165883%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-distance-notification-time-in-seconds"><span>distance</span><wbr></wbr><span>Notification</span><wbr></wbr><span>Time</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Seconds</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1182165883%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-distance-notification-time-in-seconds">distanceNotificationTimeInSeconds</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief "><p class="paragraph">The default time setting for <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.ManeuverNotificationType.DISTANCE</a> notification.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="189242472%2FProperties%2F1617540583" anchor-label="doubleNotificationDistanceInMeters" id="189242472%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-double-notification-distance-in-meters"><span>double</span><wbr></wbr><span>Notification</span><wbr></wbr><span>Distance</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Meters</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="189242472%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-double-notification-distance-in-meters">doubleNotificationDistanceInMeters</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief "><p class="paragraph">The default distance setting for double notification.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1545068422%2FProperties%2F1617540583" anchor-label="rangeNotificationDistanceInMeters" id="1545068422%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-range-notification-distance-in-meters"><span>range</span><wbr></wbr><span>Notification</span><wbr></wbr><span>Distance</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Meters</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1545068422%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-range-notification-distance-in-meters">rangeNotificationDistanceInMeters</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief "><p class="paragraph">The default distance setting for <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.ManeuverNotificationType.RANGE</a> notification. A configuration value of 0 is only allowed for <a href="sdk-for-flutter-explore-range-notification-distance-in-meters">com.here.sdk.navigation.ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters</a> and <a href="sdk-for-flutter-explore-range-notification-time-in-seconds">com.here.sdk.navigation.ManeuverNotificationTimingOptions.rangeNotificationTimeInSeconds</a>. It means that the maneuver notifications of type <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.ManeuverNotificationType.RANGE</a> should be generated as soon as the maneuver location is known - no matter how far away it may be.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-971044797%2FProperties%2F1617540583" anchor-label="rangeNotificationTimeInSeconds" id="-971044797%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-range-notification-time-in-seconds"><span>range</span><wbr></wbr><span>Notification</span><wbr></wbr><span>Time</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Seconds</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-971044797%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-range-notification-time-in-seconds">rangeNotificationTimeInSeconds</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief "><p class="paragraph">The default time setting for <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.ManeuverNotificationType.RANGE</a> notification. A configuration value of 0 is only allowed for <a href="sdk-for-flutter-explore-range-notification-distance-in-meters">com.here.sdk.navigation.ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters</a> and <a href="sdk-for-flutter-explore-range-notification-time-in-seconds">com.here.sdk.navigation.ManeuverNotificationTimingOptions.rangeNotificationTimeInSeconds</a>. It means that the maneuver notifications of type <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.ManeuverNotificationType.RANGE</a> should be generated as soon as the maneuver location is known - no matter how far away it may be.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="579859367%2FProperties%2F1617540583" anchor-label="reminderNotificationDistanceInMeters" id="579859367%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-reminder-notification-distance-in-meters"><span>reminder</span><wbr></wbr><span>Notification</span><wbr></wbr><span>Distance</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Meters</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="579859367%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-reminder-notification-distance-in-meters">reminderNotificationDistanceInMeters</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief "><p class="paragraph">The default distance setting for <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.ManeuverNotificationType.REMINDER</a> notification.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1557704766%2FProperties%2F1617540583" anchor-label="reminderNotificationTimeInSeconds" id="-1557704766%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-reminder-notification-time-in-seconds"><span>reminder</span><wbr></wbr><span>Notification</span><wbr></wbr><span>Time</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Seconds</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1557704766%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-reminder-notification-time-in-seconds">reminderNotificationTimeInSeconds</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief "><p class="paragraph">The default time setting for <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.ManeuverNotificationType.REMINDER</a> notification.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="-640799175%2FFunctions%2F1617540583" anchor-label="equals" id="-640799175%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-equals"><span><span>equals</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-640799175%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">operator override </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-equals"><span class="token function">equals</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">other<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="token operator">?</span></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2034460301%2FFunctions%2F1617540583" anchor-label="hashCode" id="2034460301%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-hash-code"><span>hash</span><wbr></wbr><span><span>Code</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2034460301%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-hash-code"><span class="token function">hashCode</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
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
