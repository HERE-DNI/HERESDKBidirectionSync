---
title: "Maneuver (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmaneuver"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class Maneuver

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.routing.Maneuver
------------------------------------------------------------------------
public final class Maneuver extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
This class provides all the information for a maneuver. The directional information (e.g. road names, road numbers and signpost direction) is stored in [`getRoadTexts()`](#getRoadTexts()) and [`getNextRoadTexts()`](#getNextRoadTexts()) attributes. As for the motorway exit information, it can be obtained from [`getExitSignTexts()`](#getExitSignTexts()) attribute.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`ManeuverAction`](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing")

  [getAction](#getAction())`()`

Gets the maneuver action.

[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")

  [getCoordinates](#getCoordinates())`()`

Gets the geographic coordinates where the maneuver is located.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getCountryCode](#getCountryCode())`()`

Gets the country code of the maneuver position.

[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [getDuration](#getDuration())`()`

Gets the estimated time in seconds needed to perform the maneuver.

[`LocalizedTexts`](sdk-for-android-explore-api-reference-latestlocalizedtexts "class in com.here.sdk.core")

  [getExitSignTexts](#getExitSignTexts())`()`

Gets the textual attributes of the exit sign.

[`LocalizedTexts`](sdk-for-android-explore-api-reference-latestlocalizedtexts "class in com.here.sdk.core")

  [getIntersectionNames](#getIntersectionNames())`()`

Gets the textual attributes of the intersection.

`int`

  [getLengthInMeters](#getLengthInMeters())`()`

Gets the length of the maneuver in meters.

[`RoadTexts`](sdk-for-android-explore-api-reference-latestroadtexts "class in com.here.sdk.routing")

  [getNextRoadTexts](#getNextRoadTexts())`()`

Gets the textual attributes of the next road containing the corresponding road name(s) and road number(s) after the maneuver point.

`int`

  [getOffset](#getOffset())`()`

Gets the index over [`Section.getGeometry()`](sdk-for-android-explore-api-reference-latestsection#getGeometry()) where the maneuver is located.

[`RoadTexts`](sdk-for-android-explore-api-reference-latestroadtexts "class in com.here.sdk.routing")

  [getRoadTexts](#getRoadTexts())`()`

Gets the textual attributes of the current road containing road names, road numbers and signpost direction (towards) information.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [getRoundaboutAngleInDegrees](#getRoundaboutAngleInDegrees())`()`

The angle is estimated between the incoming and outgoing route parts before entering the actual roundabout.

`int`

  [getSectionIndex](#getSectionIndex())`()`

Gets the index over [`Route.getSections()`](sdk-for-android-explore-api-reference-latestroute#getSections()) indicating the section to which the maneuver belongs to.

[`Signpost`](sdk-for-android-explore-api-reference-latestsignpost "class in com.here.sdk.routing")

  [getSignpost](#getSignpost())`()`

Gets [`Signpost`](sdk-for-android-explore-api-reference-latestsignpost "class in com.here.sdk.routing") object.

`int`

  [getSpanIndex](#getSpanIndex())`()`

Gets the index over [`Section.getSpans()`](sdk-for-android-explore-api-reference-latestsection#getSpans()) indicating the first span after the maneuver point.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getText](#getText())`()`

Gets the maneuver instruction.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [getTurnAngleInDegrees](#getTurnAngleInDegrees())`()`

Gets the angle of the turn component of the maneuver.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### getAction

@NonNull public [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") getAction()

    Gets the maneuver action.
Returns:
    Indicates the maneuver action.

### getCoordinates

@NonNull public [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") getCoordinates()

    Gets the geographic coordinates where the maneuver is located.
Returns:
    Geographic coordinates where the maneuver is located.

### getOffset

public int getOffset()

    Gets the index over [`Section.getGeometry()`](sdk-for-android-explore-api-reference-latestsection#getGeometry()) where the maneuver is located.
Returns:
    Index over [`Section.getGeometry()`](sdk-for-android-explore-api-reference-latestsection#getGeometry()) where the maneuver is located.

### getCountryCode

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getCountryCode()

    Gets the country code of the maneuver position. The value is `null` when no data is available.
Returns:
    The country code of the maneuver position. The value is `null` when no data is available.

### getExitSignTexts

@NonNull public [LocalizedTexts](sdk-for-android-explore-api-reference-latestlocalizedtexts "class in com.here.sdk.core") getExitSignTexts()

    Gets the textual attributes of the exit sign. These might contain exit number(s) and/or name(s).

    These attributes are only available for the Navigate license. Otherwise, the attributes are always empty.
Returns:
    The textual attributes of the exit sign. These might contain exit number(s) and/or name(s).

### getLengthInMeters

public int getLengthInMeters()

    Gets the length of the maneuver in meters.
Returns:
    The length of the maneuver in meters.

### getRoadTexts

@NonNull public [RoadTexts](sdk-for-android-explore-api-reference-latestroadtexts "class in com.here.sdk.routing") getRoadTexts()

    Gets the textual attributes of the current road containing road names, road numbers and signpost direction (towards) information.

    **Note:** These attributes are only available for the Navigate license. Otherwise, the attributes are always empty.
Returns:
    The textual attributes of the current road containing road names, road numbers and signpost direction (towards) information.

### getNextRoadTexts

@NonNull public [RoadTexts](sdk-for-android-explore-api-reference-latestroadtexts "class in com.here.sdk.routing") getNextRoadTexts()

    Gets the textual attributes of the next road containing the corresponding road name(s) and road number(s) after the maneuver point.

    These attributes are only available for the Navigate license. Otherwise, the attributes are always empty.
Returns:
    The textual attributes of the next road containing the corresponding road name(s) and road number(s) after the maneuver point.

### getSignpost

@Nullable public [Signpost](sdk-for-android-explore-api-reference-latestsignpost "class in com.here.sdk.routing") getSignpost()

    Gets [`Signpost`](sdk-for-android-explore-api-reference-latestsignpost "class in com.here.sdk.routing") object.
Returns:
    Gets the [`Signpost`](sdk-for-android-explore-api-reference-latestsignpost "class in com.here.sdk.routing") object.

### getIntersectionNames

@NonNull public [LocalizedTexts](sdk-for-android-explore-api-reference-latestlocalizedtexts "class in com.here.sdk.core") getIntersectionNames()

    Gets the textual attributes of the intersection.

    These attributes are only available for the Navigate license. Otherwise, the attributes are always empty. **Note:** Routes calculated with OfflineRoutingEngine are not supported.
Returns:
    The textual attributes of the intersection.

### getText

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getText()

    Gets the maneuver instruction. The text is formatted and localized as specified via [`RouteTextOptions`](sdk-for-android-explore-api-reference-latestroutetextoptions "class in com.here.sdk.routing").

    **Note for users of the Navigate license:** This text is meant to be displayed in a preview context, whereas real-time `EventTextListener` texts are meant to be used for spoken voice announcements during a trip.
Returns:
    The maneuver instruction. The text is formatted and localized as specified via [`RouteTextOptions`](sdk-for-android-explore-api-reference-latestroutetextoptions "class in com.here.sdk.routing").

### getSectionIndex

public int getSectionIndex()

    Gets the index over [`Route.getSections()`](sdk-for-android-explore-api-reference-latestroute#getSections()) indicating the section to which the maneuver belongs to.
Returns:
    Index over [`Route.getSections()`](sdk-for-android-explore-api-reference-latestroute#getSections()) indicating the section to which the maneuver belongs to.

### getSpanIndex

public int getSpanIndex()

    Gets the index over [`Section.getSpans()`](sdk-for-android-explore-api-reference-latestsection#getSpans()) indicating the first span after the maneuver point.

    **Note:** The span index for the last maneuvers (those maneuvers with maneuver action set to [`ManeuverAction.ARRIVE`](sdk-for-android-explore-api-reference-latestmaneuveraction#ARRIVE)) cannot be used, since these maneuvers are placed after the last span of the route and the span index for them would be greater than the span list size.
Returns:
    Index over [`Section.getSpans()`](sdk-for-android-explore-api-reference-latestsection#getSpans()) indicating the first span after the maneuver point.

### getDuration

@NonNull public [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") getDuration()

    Gets the estimated time in seconds needed to perform the maneuver.
Returns:
    The estimated time in seconds needed to perform the maneuver.

### getTurnAngleInDegrees

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) getTurnAngleInDegrees()

    Gets the angle of the turn component of the maneuver. The value is in degrees and from -180 to 180.

    The angle increases clockwise and small values are used for going straight, i.e. a positive number means there is a right turn and a negative number is a left turn. Some maneuvers like Depart, Arrive and Roundabout pass doesn't have a well defined angle, so the value is omitted. **Note:** These attributes are only available for the Navigate license.
Returns:
    The angle of the turn component of the maneuver.

### getRoundaboutAngleInDegrees

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) getRoundaboutAngleInDegrees()

    The angle is estimated between the incoming and outgoing route parts before entering the actual roundabout.

    This is done to provide a better orientation for drivers. For better results, the incoming and outcoming route parts can be around 50 meters in length. In addition, these parts lie usually around 30 meters away from the actual roundabout. Therefore, the resulting arc does not necessarily represent the exact curved path a vehicle has to follow within a roundabout from the point of entry to the point of exit. Instead, it reflects the route path before and after the roundabout to highlight the directional change along the route. The angle can have a value from -360.0 to 360.0, and it is positive in right-hand side driving country, and negative in left-hand side countries. Note that the value is available for both the enter roundabout actions and the exit roundabout actions. Both maneuvers have the same value. When the incoming or outgoing route parts are curvy or when the roundabout itself is not representing a perfect circle, then the accuracy of the angle may be compromised. **Note:** These attributes are only available for the Navigate license.
Returns:
    The angle is estimated between the incoming and outgoing route parts before entering the actual roundabout.
