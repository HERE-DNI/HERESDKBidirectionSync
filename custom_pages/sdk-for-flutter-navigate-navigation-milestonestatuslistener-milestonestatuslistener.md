---
title: "MilestoneStatusListener constructor - MilestoneStatusListener - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-milestonestatuslistener-milestonestatuslistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/MilestoneStatusListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MilestoneStatusListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MilestoneStatusListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onMilestoneStatusUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onMilestoneStatusUpdatedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-milestone-class">Milestone</a></span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-milestonestatus">MilestoneStatus</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive notifications from this class about the arrival at each <a href="sdk-for-flutter-navigate-navigation-milestone-class">Milestone</a> or missing it.

</div>

## Implementation

``` dart
factory MilestoneStatusListener(
  void Function(Milestone, MilestoneStatus) onMilestoneStatusUpdatedLambda,

) => MilestoneStatusListener$Lambdas(
  onMilestoneStatusUpdatedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

