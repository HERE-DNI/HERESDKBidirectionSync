---
title: "ManeuverNotificationOptions constructor"
slug: "sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-maneuvernotificationoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ManeuverNotificationOptions.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-class</li>
<li class="self-crumb">ManeuverNotificationOptions constructor</li>
</ol>
<div class="self-name">ManeuverNotificationOptions</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="navigation/ManeuverNotificationOptions-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>ManeuverNotificationOptions constructor</h1></div>
<section class="multi-line-signature">
<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.23.0. Use the withDefaults instead.")</li>
</ol>
</div>
ManeuverNotificationOptions(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-languagecode language, </li>
<li>/sdk-for-flutter-navigate-core-unitsystem unitSystem</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a new instance of this class with specified language and unit system.</p>
<ul>
<li><code>language</code> The language in which the notifications will be generated. When the specified language
is not supported, the default language is used, which is English (American).</li>
<li><code>unitSystem</code> Defines the measurement system used for distances. Defaults to metric.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.23.0. Use the withDefaults instead.")
ManeuverNotificationOptions(this.language, this.unitSystem)
    : includedNotificationTypes = [ManeuverNotificationType.range, ManeuverNotificationType.reminder, ManeuverNotificationType.distance, ManeuverNotificationType.action], enableRoundaboutNotification = true, enableDestinationReachedNotification = true, arrivalNotificationOption = ArrivalNotificationOption.both, enableDoubleNotification = true, enablePhoneme = false, notificationFormatOption = NotificationFormatOption.plain, textUsageOptions = TextUsageOptions(), enableHighwayExit = true, enableLaneRecommendation = false, includedNaturalGuidanceTypes = [], directionInformationUsageForActionNotificationOption = DirectionInformationUsageOption.none;</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-class</li>
<li class="self-crumb">ManeuverNotificationOptions constructor</li>
</ol>
<h5>ManeuverNotificationOptions class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
`
}</HTMLBlock>
