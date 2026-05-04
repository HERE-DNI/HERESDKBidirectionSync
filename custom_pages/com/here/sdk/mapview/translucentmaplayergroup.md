---
title: "TranslucentMapLayerGroup (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttranslucentmaplayergroup"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TranslucentMapLayerGroup

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.TranslucentMapLayerGroup
------------------------------------------------------------------------
public final class TranslucentMapLayerGroup extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
A translucent layer group that can be the target for [`MapLayerPriorityBuilder.inGroup(java.lang.String)`](sdk-for-android-explore-api-reference-latestmaplayerprioritybuilder#inGroup(java.lang.String)). Currently, only custom line layers can be added to a translucent layer group. Custom line layers in a translucent layer group are rendered in an offscreen translucent pass so that overlapping translucent line geometry is not alpha blended with itself. At creation, the layer group gets added to a map. The layer group gets removed from the map upon instance destruction and any layer (categories) still in the group are not rendered anymore, therefore it is recommended to keep a group alive as long as layers using the group are alive and in use.

Conceptual example to place line layers into a translucent group:

    // Create a translucent group with a unique name and a render priority
      MapLayerPriority groupPriority = new MapLayerPriorityBuilder().renderedLast().build();
      TranslucentMapLayerGroup group = new TranslucentMapLayerGroup("TranslucentGroupName", map, groupPriority)

      // Create a line layer to be rendered as part of the translucent group
      MapLayerPriority lineLayerPriority = new MapLayerPriorityBuilder()
          .inGroup("TranslucentGroupName") // places the line layer into the group
          .renderedFirst()                 // to be rendered first when the group is rendered
          .withCategory("SomeCategory")    // places the line layer category 'SomeCategory'
          .inGroup("TranslucentGroupName") // into the group
          .renderedLast()                  // to be rendered last when the group is rendered
          .build();

      MapLayer lineLayer = new MapLayerBuilder()
          .withDataSource("DataSourceName", MapContentType.LINE)
          .forMap(map)
          .withName("LineLayerName")
          .withPriority(lineLayerPriority)
          .withStyle(translucentLineStyle) // E.g. "technique": "line" ... "color": "#FFFFFF80"
          .build();

      // Create a second line layer to be rendered as part of the translucent group
      MapLayerPriority secondLineLayerPriority = new MapLayerPriorityBuilder()
          .inGroup("TranslucentGroupName")      // places the second line layer into the group
          .renderedBeforeLayer("LineLayerName") // to be rendered before first layer
                                                // when the group is rendered
          .build();

      MapLayer secondLineLayer = new MapLayerBuilder()
          .withDataSource("SecondDataSourceName", MapContentType.LINE)
          .forMap(map)
          .withName("SecondLineLayerName")
          .withPriority(secondLineLayerPriority)
          .withStyle(secondTranslucentLineStyle) // E.g. "technique": "line" ... "color": "#FFFFFF80"
          .build();

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static enum `

  [TranslucentMapLayerGroup.ErrorCode](sdk-for-android-explore-api-reference-latesttranslucentmaplayergroup-errorcode)

Error codes for creating the group.

`static final class `

  [TranslucentMapLayerGroup.ErrorDetails](sdk-for-android-explore-api-reference-latesttranslucentmaplayergroup-errordetails)

Describes the reason for failing to create the group.

`static final class `

  [TranslucentMapLayerGroup.InstantiationException](sdk-for-android-explore-api-reference-latesttranslucentmaplayergroup-instantiationexception)

Thrown when failing to build the group.

## Constructor Summary

Constructors

Constructor

  Description

  [TranslucentMapLayerGroup](#%3Cinit%3E(java.lang.String,com.here.sdk.mapview.HereMap))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name, `[`HereMap`](sdk-for-android-explore-api-reference-latestheremap "class in com.here.sdk.mapview")` aMap)`

Creates an instance of the group.

[TranslucentMapLayerGroup](#%3Cinit%3E(java.lang.String,com.here.sdk.mapview.HereMap,com.here.sdk.mapview.MapLayerPriority))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name, `[`HereMap`](sdk-for-android-explore-api-reference-latestheremap "class in com.here.sdk.mapview")` aMap, `[`MapLayerPriority`](sdk-for-android-explore-api-reference-latestmaplayerpriority "class in com.here.sdk.mapview")` priority)`

Creates an instance of the group.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `void`

  [destroy](#destroy())`()`

Frees all internally used resources.

`void`

  [setPriority](#setPriority(com.here.sdk.mapview.MapLayerPriority))`(`[`MapLayerPriority`](sdk-for-android-explore-api-reference-latestmaplayerpriority "class in com.here.sdk.mapview")` priority)`

Sets the render priority for the layer group which replaces any previously defined priority.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - (java.lang.String,com.here.sdk.mapview.HereMap)" class="section detail">

### TranslucentMapLayerGroup

public TranslucentMapLayerGroup(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name, @NonNull [HereMap](sdk-for-android-explore-api-reference-latestheremap "class in com.here.sdk.mapview") aMap) throws [TranslucentMapLayerGroup.InstantiationException](sdk-for-android-explore-api-reference-latesttranslucentmaplayergroup-instantiationexception "class in com.here.sdk.mapview")

    Creates an instance of the group.
Parameters:
    `name` -

    Name of the group. Must be unique across [`MapLayer`](sdk-for-android-explore-api-reference-latestmaplayer "class in com.here.sdk.mapview") and [`TranslucentMapLayerGroup`](sdk-for-android-explore-api-reference-latesttranslucentmaplayergroup "class in com.here.sdk.mapview").

    `aMap` -

    The map to attach the group to.

    Throws:
    [`TranslucentMapLayerGroup.InstantiationException`](sdk-for-android-explore-api-reference-latesttranslucentmaplayergroup-instantiationexception "class in com.here.sdk.mapview") -

    In case of invalid input parameters.
- (java.lang.String,com.here.sdk.mapview.HereMap,com.here.sdk.mapview.MapLayerPriority)" class="section detail">

### TranslucentMapLayerGroup

public TranslucentMapLayerGroup(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name, @NonNull [HereMap](sdk-for-android-explore-api-reference-latestheremap "class in com.here.sdk.mapview") aMap, @NonNull [MapLayerPriority](sdk-for-android-explore-api-reference-latestmaplayerpriority "class in com.here.sdk.mapview") priority) throws [TranslucentMapLayerGroup.InstantiationException](sdk-for-android-explore-api-reference-latesttranslucentmaplayergroup-instantiationexception "class in com.here.sdk.mapview")

    Creates an instance of the group.
Parameters:
    `name` -

    Name of the group. Must be unique across [`MapLayer`](sdk-for-android-explore-api-reference-latestmaplayer "class in com.here.sdk.mapview") and [`TranslucentMapLayerGroup`](sdk-for-android-explore-api-reference-latesttranslucentmaplayergroup "class in com.here.sdk.mapview").

    `aMap` -

    The map to attach the group to.

    `priority` -

    The [`MapLayerPriority`](sdk-for-android-explore-api-reference-latestmaplayerpriority "class in com.here.sdk.mapview") which should be applied to position the group. The [`MapLayerPriority`](sdk-for-android-explore-api-reference-latestmaplayerpriority "class in com.here.sdk.mapview") must contain only one priority and this priority must have no category and no group, i.e. [`MapLayerPriorityBuilder.inGroup(java.lang.String)`](sdk-for-android-explore-api-reference-latestmaplayerprioritybuilder#inGroup(java.lang.String)) and [`MapLayerPriorityBuilder.withCategory(java.lang.String)`](sdk-for-android-explore-api-reference-latestmaplayerprioritybuilder#withCategory(java.lang.String)) should not be used when building the [`MapLayerPriority`](sdk-for-android-explore-api-reference-latestmaplayerpriority "class in com.here.sdk.mapview"). Example:

    `new MapLayerPriorityBuilder().renderedAfterLayer(&quot;water&quot;).build()`

    Throws:
    [`TranslucentMapLayerGroup.InstantiationException`](sdk-for-android-explore-api-reference-latesttranslucentmaplayergroup-instantiationexception "class in com.here.sdk.mapview") -

    In case of invalid input parameters.

## Method Details

### setPriority

public void setPriority(@NonNull [MapLayerPriority](sdk-for-android-explore-api-reference-latestmaplayerpriority "class in com.here.sdk.mapview") priority)

    Sets the render priority for the layer group which replaces any previously defined priority.
Parameters:
    `priority` -

    The priority to position the group. The [`MapLayerPriority`](sdk-for-android-explore-api-reference-latestmaplayerpriority "class in com.here.sdk.mapview") must contain only one priority and this priority must have no category and no group, i.e. [`MapLayerPriorityBuilder.inGroup(java.lang.String)`](sdk-for-android-explore-api-reference-latestmaplayerprioritybuilder#inGroup(java.lang.String)) and [`MapLayerPriorityBuilder.withCategory(java.lang.String)`](sdk-for-android-explore-api-reference-latestmaplayerprioritybuilder#withCategory(java.lang.String)) should not be used when building the [`MapLayerPriority`](sdk-for-android-explore-api-reference-latestmaplayerpriority "class in com.here.sdk.mapview"). Example:

    `new MapLayerPriorityBuilder().renderedAfterLayer(&quot;water&quot;).build()`

### destroy

public void destroy()

    Frees all internally used resources. After calling this method, the object is not usable anymore.
