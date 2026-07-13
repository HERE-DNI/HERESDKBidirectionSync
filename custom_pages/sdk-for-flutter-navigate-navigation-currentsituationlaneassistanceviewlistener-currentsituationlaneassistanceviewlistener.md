---
title: "CurrentSituationLaneAssistanceViewListener constructor - CurrentSituationLaneAssistanceViewListener - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-currentsituationlaneassistanceviewlistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/CurrentSituationLaneAssistanceViewListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">CurrentSituationLaneAssistanceViewListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">CurrentSituationLaneAssistanceViewListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onCurrentSituationLaneAssistanceViewUpdateLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onCurrentSituationLaneAssistanceViewUpdateLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceview-class">CurrentSituationLaneAssistanceView</a></span></span>

    )</span>

)

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

## Implementation

``` dart
factory CurrentSituationLaneAssistanceViewListener(
  void Function(CurrentSituationLaneAssistanceView) onCurrentSituationLaneAssistanceViewUpdateLambda,

) => CurrentSituationLaneAssistanceViewListener$Lambdas(
  onCurrentSituationLaneAssistanceViewUpdateLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

