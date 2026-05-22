---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-setwarningnotificationdistances"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setWarningNotificationDistances.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-navigatorinterface-class</li>
<li class="self-crumb">setWarningNotificationDistances abstract method</li>
</ol>
<div class="self-name">setWarningNotificationDistances</div>
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
<div class="main-content" data-above-sidebar="navigation/NavigatorInterface-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>setWarningNotificationDistances abstract method</h1></div>
<section class="multi-line-signature">
bool
setWarningNotificationDistances(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-warningtype warningType, </li>
<li>/sdk-for-flutter-navigate-navigation-warningnotificationdistances-class warningNotificationDistances</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Set the warning notification distances for the specified warning types.</p>
<p><strong>Note:</strong> The warning notification distances are set for most warners.
This method can't be used to set the warning notification distance for the School Zone warning type because it is applicable regardless of the timing profile. Use <code>NavigatorInterface.school_zone_warning_options</code> instead.
Attempting to set the warning notification distances for the school zone warner using the <code>NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code>false</code>.
Always use <code>SchoolZoneWarningOptions.warning_distance_in_meters</code> to set the warning notification distance for the school zone warner regardless of the <code>TimingProfile</code>.
If <code>NavigatorInterface.set_warning_notification_distances</code> could be used, this would allow for different distances to be set for each timing profile, which is undesirable.
Attempting to set the warning notification distances for the traffic merge warner using the <code>NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code>false</code>.
Always use <code>TrafficMergeWarningOptions.warning_distance_in_meters</code> to set the warning notification distance for the traffic merge warner regardless of the <code>TimingProfile</code>.
Using the <code>NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code>false</code> to avoid
seting different distances on each timing profile since the traffic merge warning is only applicable on highways.</p>
<ul>
<li>
<p><code>warningType</code> The warning type for which the warning notification distances will be set.</p>
</li>
<li>
<p><code>warningNotificationDistances</code> The warning notification distances to be set for the specified warning types.</p>
</li>
</ul>
<p>Returns <code>bool</code>. <code>True</code> if set successfully, <code>false</code> when the warning_type is <code>WarningType.SCHOOL_ZONE</code> or the options have invalid values,
see /sdk-for-flutter-navigate-navigation-warningnotificationdistances-class for more details about warning notification distances.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool setWarningNotificationDistances(WarningType warningType, WarningNotificationDistances warningNotificationDistances);</code></pre>
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
<li>/sdk-for-flutter-navigate-navigation-navigatorinterface-class</li>
<li class="self-crumb">setWarningNotificationDistances abstract method</li>
</ol>
<h5>NavigatorInterface class</h5>
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
