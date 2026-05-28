---
title: "CurrentSituationLaneAssistanceViewListener constructor"
slug: "sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-currentsituationlaneassistanceviewlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CurrentSituationLaneAssistanceViewListener.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-class</li>
<li class="self-crumb">CurrentSituationLaneAssistanceViewListener factory constructor</li>
</ol>
<div class="self-name">CurrentSituationLaneAssistanceViewListener</div>
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
<div class="main-content" data-above-sidebar="navigation/CurrentSituationLaneAssistanceViewListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>CurrentSituationLaneAssistanceViewListener constructor</h1></div>
<section class="multi-line-signature">
CurrentSituationLaneAssistanceViewListener(<wbr/><ol class="parameter-list single-line"> <li>void onCurrentSituationLaneAssistanceViewUpdateLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceview-class</li>
</ol>)</li>
</ol>)
    </section>
<section class="desc markdown">
<p>This abstract class should be
implemented in order to receive notifications on /sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceview-class.</p>
<p>The current situation lane assistance view notifications describe the lane information at the current location.</p>
<p>A new notification is evaluated with each location update. A notification is only sent when there is a change
in lane data, such as a new upcoming lane.</p>
<p>This event is supported both with a route during turn-by-turn navigation and without a route in tracking mode.
During turn-by-turn navigation, the event additionally indicates which lanes help the driver stay on the route
to reach the destination.
However, the event does not indicate which exact lane the user is currently driving in.
The listener works for offline mode as well.</p>
<p><strong>Note:</strong></p>
<ul>
<li>Lane information is not available for all roads. It's mostly available for roads with painted turn directions.</li>
<li>This is a <strong>beta</strong> release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory CurrentSituationLaneAssistanceViewListener(
  void Function(CurrentSituationLaneAssistanceView) onCurrentSituationLaneAssistanceViewUpdateLambda,

) =&gt; CurrentSituationLaneAssistanceViewListener$Lambdas(
  onCurrentSituationLaneAssistanceViewUpdateLambda,

);</code></pre>
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
<li>/sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-class</li>
<li class="self-crumb">CurrentSituationLaneAssistanceViewListener factory constructor</li>
</ol>
<h5>CurrentSituationLaneAssistanceViewListener class</h5>
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
