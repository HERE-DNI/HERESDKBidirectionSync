---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-maneuvernotificationoptions-withallfieldsnew"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ManeuverNotificationOptions.withAllFieldsNew.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-class</li>
<li class="self-crumb">ManeuverNotificationOptions.withAllFieldsNew constructor</li>
</ol>
<div class="self-name">ManeuverNotificationOptions.withAllFieldsNew</div>
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
<h1>ManeuverNotificationOptions.withAllFieldsNew constructor</h1></div>
<section class="multi-line-signature">
<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.23.0. Use the <code>withDefaults</code> instead.")</li>
</ol>
</div>
ManeuverNotificationOptions.withAllFieldsNew(<wbr/><ol class="parameter-list"> <li>/sdk-for-flutter-navigate-core-languagecode language, </li>
<li>/sdk-for-flutter-navigate-core-unitsystem unitSystem, </li>
<li>List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-maneuvernotificationtype&gt; includedNotificationTypes, </li>
<li>bool enableRoundaboutNotification, </li>
<li>bool enableDestinationReachedNotification, </li>
<li>bool enableDoubleNotification, </li>
<li>bool enablePhoneme, </li>
<li>/sdk-for-flutter-navigate-navigation-notificationformatoption notificationFormatOption, </li>
<li>bool enableHighwayExit, </li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a new instance of this class with full specified configurations.</p>
<ul>
<li><code>language</code> The language in which the notifications will be generated. When the specified language
is not supported, the default language is used, which is English (American).</li>
<li><code>unitSystem</code> Defines the measurement system used for distances. Defaults to metric.</li>
<li><code>includedNotificationTypes</code> List of /sdk-for-flutter-navigate-navigation-maneuvernotificationtype for which notifications should be generated. Excluding all of
them will disable the maneuver notifications completely.
By default, all types are included.</li>
<li><code>enableRoundaboutNotification</code> A flag that indicates whether notification for roundabout-related maneuvers should be generated.
Defaults to <code>true</code>.</li>
<li><code>enableDestinationReachedNotification</code> A flag that indicates whether notification for destination/stopover reached maneuvers should be generated.
Defaults to <code>true</code>.</li>
<li><code>enableDoubleNotification</code> A flag that indicates whether combined maneuver notifications should be generated.
Such double notifications can be useful when maneuvers are very close.
<strong>Example:</strong> A combined message: 'After 300 meters turn left and then turn right.'.
This way a user can better anticipate the next-next maneuver.
Note that setting to <code>true</code> will make the notification longer as two maneuvers will be merged into one.
When the next-next maneuver action takes place, the notification will be given as usual.
<strong>Example:</strong> 'Now turn left and then then turn right.' will be followed by 'Now turn right.'.
Defaults to <code>true</code>.</li>
<li><code>enablePhoneme</code> A flag that indicates whether phonemes in selected notification format for proper nouns (e.g. road names,
road numbers, city names) should be used when generating notifications. Direction information comes usually
in orthographic form and phoneme (e.g. Wall Street and "wɔːl"striːt). However, when the notification is
synthesized by a TTS engine, the pronunciation of the orthographic form solely depends on its capability
and phoneme set. The use of our phoneme data in the notification usually makes the pronunciation of
direction information sound more natural.
<strong>Note:</strong> For now, this property is functional for road name and road number information only.</li>
</ul>
<p>Defaults to <code>false</code>.</p>
<ul>
<li><code>notificationFormatOption</code> A formatting option for the phoneme that is included in the notification. By default, no phoneme is used
and the /sdk-for-flutter-navigate-navigation-notificationformatoption orthographic form is included in the notification.</li>
</ul>
<p><strong>Note:</strong>
To use the SSML format for phonemes, /sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-enablephoneme needs to be set to <code>true</code>.</p>
<ul>
<li><code>enableHighwayExit</code> A flag that indicates whether highway exit information should be used when generating notification.
Defaults to <code>true</code>.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.23.0. Use the `withDefaults` instead.")
ManeuverNotificationOptions.withAllFieldsNew(this.language, this.unitSystem, this.includedNotificationTypes, this.enableRoundaboutNotification, this.enableDestinationReachedNotification, this.enableDoubleNotification, this.enablePhoneme, this.notificationFormatOption, this.enableHighwayExit)
    : arrivalNotificationOption = ArrivalNotificationOption.both, textUsageOptions = TextUsageOptions(), enableLaneRecommendation = false, includedNaturalGuidanceTypes = [], directionInformationUsageForActionNotificationOption = DirectionInformationUsageOption.none;</code></pre>
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
<li class="self-crumb">ManeuverNotificationOptions.withAllFieldsNew constructor</li>
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



</div>
`
}</HTMLBlock>
