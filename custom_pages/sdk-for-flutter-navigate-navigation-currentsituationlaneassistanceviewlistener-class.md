---
title: "CurrentSituationLaneAssistanceViewListener class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CurrentSituationLaneAssistanceViewListener-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/CurrentSituationLaneAssistanceViewListener-class-sidebar.html">

<div>

# <span class="kind-class">CurrentSituationLaneAssistanceViewListener</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive notifications on <a href="sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceview-class">CurrentSituationLaneAssistanceView</a>.

The current situation lane assistance view notifications describe the lane information at the current location.

A new notification is evaluated with each location update. A notification is only sent when there is a change in lane data, such as a new upcoming lane.

This event is supported both with a route during turn-by-turn navigation and without a route in tracking mode. During turn-by-turn navigation, the event additionally indicates which lanes help the driver stay on the route to reach the destination. However, the event does not indicate which exact lane the user is currently driving in. The listener works for offline mode as well.

**Note:**

- Lane information is not available for all roads. It's mostly available for roads with painted turn directions.
- This is a **beta** release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-currentsituationlaneassistanceviewlistener">CurrentSituationLaneAssistanceViewListener</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-onCurrentSituationLaneAssistanceViewUpdateLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onCurrentSituationLaneAssistanceViewUpdateLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceview-class">CurrentSituationLaneAssistanceView</a></span></span>)</span>)</span>  
This abstract class should be implemented in order to receive notifications on <a href="sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceview-class">CurrentSituationLaneAssistanceView</a>.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-oncurrentsituationlaneassistanceviewupdate">onCurrentSituationLaneAssistanceViewUpdate</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onCurrentSituationLaneAssistanceViewUpdate-param-lanes" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceview-class">CurrentSituationLaneAssistanceView</a></span> <span class="parameter-name">lanes</span></span>) <span class="returntype parameter">→ void</span> </span>  
The callback to be called.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
