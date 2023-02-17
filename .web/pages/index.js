import {useEffect, useRef, useState} from "react"
import {useRouter} from "next/router"
import {E, connect, updateState} from "/utils/state"
import "focus-visible/dist/focus-visible"
import {Box, Button, Drawer, DrawerBody, DrawerContent, DrawerFooter, DrawerHeader, DrawerOverlay, Text, VStack} from "@chakra-ui/react"
import NextHead from "next/head"

const EVENT = "ws://localhost:8000/event"
export default function Component() {
const [drawer_state, setDrawer_state] = useState({"show_right": false, "show_top": false, "events": [{"name": "drawer_state.hydrate"}]})
const [result, setResult] = useState({"state": null, "events": [], "processing": false})
const router = useRouter()
const socket = useRef(null)
const { isReady } = router;
const Event = events => setDrawer_state({
  ...drawer_state,
  events: [...drawer_state.events, ...events],
})
useEffect(() => {
  if(!isReady)
    return;
  if (!socket.current) {
    connect(socket, drawer_state, result, setResult, router, EVENT)
  }
  const update = async () => {
    if (result.state != null) {
      setDrawer_state({
        ...result.state,
        events: [...drawer_state.events, ...result.events],
      })
      setResult({
        state: null,
        events: [],
        processing: false,
      })
    }
    await updateState(drawer_state, result, setResult, router, socket.current)
  }
  update()
})
return (
<VStack>
<Box>
<Text>
{`1`}</Text></Box>
<Box>
<Text>
{`2`}</Text></Box>
<Box>
<Text>
{`3`}</Text></Box>
<Box>
<Button onClick={() => Event([E("drawer_state.right", {})])}>
{`Show Right Drawer`}</Button>
<Drawer isOpen={drawer_state.show_right}
onOverlayClick={() => Event([E("drawer_state.close", {})])}>
<DrawerOverlay>
<DrawerContent>
<DrawerHeader>
{`Confirm`}</DrawerHeader>
<DrawerBody>
{`Do you want to confirm example?`}</DrawerBody>
<DrawerFooter/></DrawerContent></DrawerOverlay></Drawer></Box>
<NextHead>
<title>{`Pynecone App`}</title>
<meta content="A Pynecone app."
name="description"/>
<meta property="og:image"
content="favicon.ico"/></NextHead></VStack>
)
}