# sehar_hosseinzade_por_finaly

import numpy as np


class Device:
    def __init__(self,topic):
        
        self.topic=topic
        
        self.topic_list=topic.split('/')
        
        self.location=self.topic_list[0]
        
        #group--->kojas kojaye khone
        self.group=self.topic_list[1]
        
        self.device_type=self.topic_list[2]
        
        self.name=self.topic_list[3]
        self.status='off'
    def __str__(self):
        return f'[{self.location},{self.group},{self.device_type},{self.name},{self.status}]'
    def turn_on(self):
        self.status='on'
        print('yes it is on')
            
    def turn_off(self):
        self.status='off'
                  
    def get_status(self):
        return self.status
        print('now it is turned off')

   

class Sensor:
    def __init__(self,topic):
        self.topic=topic
        self.topic_list=topic.split('/')
        self.name=self.topic_list[0]
        self.group=self.topic_list[1]
        self.pin=self.topic_list[2]
        self.unit=self.topic_list[3]
        self.current_value=None
    def read_sensor(self):
        return np.random.uniform(20,25)
    def __str__(self):
        return f'[{self.name}','{self.group}','{self.pin}','{self.unit}','{self.current_value}]'

    
class admin_panel():
      def __init__(self):
          self.groups={}
###### in ja ro moshkel darammmmmm str
      def __str__(self):
           return f'{self.group.name}:{self.groups}'   
          
      def create_group(self,group_name):
          
          if group_name not in self.groups:
              self.groups[group_name]=[]
              print(f'group {group_name} is created')
              
          else:
              print('your name is dublicated')
          
          
      def add_device_to_group(self,group_name,device):
       
          s='/'
          b=device.count(s)
       
          if b!=0:
              new_device=Device(device)
             
              if group_name in self.groups:
                  self.groups[group_name].append(new_device)
                  print(f'{new_device} append to {group_name} group')
          else:
         
            if group_name in self.groups:
                self.groups[group_name].append(device)
                print(f'{new_device} append to {group_name} group')
              

            else:
              print('your group is not created')
        
              
              
      def create_device(self,group_name,device_type,name):
          
          if group_name in self.groups:
              topic=f'home/{group_name}/{device_type}/{name}'
              new_device=topic
  
              self.add_device_to_group(group_name, new_device)
              print(f'new_device {name} is created')
              
          else:
              print('your group is not created')
              
              
              
      def create_multiple_devices(self,group_name,device_type,number_of_devcies):
          
          if group_name in self.groups:
              
              for i in range(1,number_of_devcies+1):
                  #number=10 -> 1,2,3,4,5,6,7,8,9,10 -->i
                  
                  device_name=f'{device_type}{i}'
                  
                  topic=f'home/{group_name}/{device_type}/{device_name}'
                  
                  new_device=Device(topic)
                  
                  self.add_device_to_group(group_name, new_device)
                  print(f'device {new_device[3]} is created')
              
          else:
              print('your group is not created')
              
              
              
      def get_devices_in_groups(self,group_name):
          if group_name in self.groups:
              return self.groups[group_name] 
              
              
          else:
              print('your group is not created')
              
              
              #tamame device haye yek grooh ro roshan koen
      def turn_on_all_in_groups(self,group_name):
          
          devices=self.get_devices_in_groups(group_name)
         
          for device in devices:
              device.turn_on()
              print(f'{device} is turn on')
              
          else:
            print('your device is not created')
              
              
      def turn_off_all_in_groups(self,group_name):
         devices=self.get_devices_in_groups(group_name)
        
         for device in devices:
             device.turn_off()
             print(f'{device} is turn off')
        
         else:
          print('your device is not created')

      def turn_on_all_devices(self,device_type):
          devices=self.get_devices_in_groups(device_type)
          for device in devices:
              device.turn_on()
              print(f'{device} is turn on')
              
          else:
             print('your device is not created')
         
      def turn_off_all_devices(self,device_type):
          devices=self.get_devices_in_groups(device_type)
          for device in devices:
              device.turn_off()
              print(f'{device} is turn off ')
              
          else:
             print('your device is not created')
         
      def get_status_in_group(self,gorup_name):
          devices=self.get_devices_in_groups(gorup_name)
          
          for device in devices:
              s=device.status()
              print(f'{device}  status is {s}')
              
          else:
            print('your device is not created')
#### ino daram rosh kar moikonam       
      def displaying_groups(self):
          keys=self.groups.keys()
          print(keys) 
          for key in keys:
              values=self.groups.get(key)
              print(values)
#### in ja ro ham moshkel daram chon dorost namayesh nemide
      def get_status_in_device_type(self,device_type):
          for devices in self.groups.values():
              for device in devices:
                  for dev in device:
                      if dev[2]==device_type:
                          print(f'device{dev[3]} is status {dev[4]}')
                      else :
                          print(f'deevice{dev[3]} is not in home')
        
         
         
      def create_sensor(self,name,group,unit,pin):
         if group in self.groups:
             new_sensor=f'{name}/{group}/{unit}/{pin}'
             print(new_sensor)
             self.add_sensor_in_group(group,new_sensor)
             print(f'sensor {name} is created')
             
         else:
             print('your group is not created')
             
      
      def add_sensor_in_group(self,group_name,sensor):
          
          s='/'
          b=sensor.count(s)
     
          if b!=0:
              new_sensor=Sensor(sensor)
              if group_name in self.groups:
                  self.groups[group_name].append(new_sensor)
                  print(f'{new_sensor} append to {group_name} group')
          else:
           
            if group_name in self.groups:
                self.groups[group_name].append(sensor)
                print(f'{sensor} append to {group_name} group')
              

            else:
              print('your group is not created')
              
      
      def get_data_from_sensor_in_group(self,sensor):
         sensors=self.get_devices_in_groups(sensor)
         print(f'{sensors} find in the group')
         return sensors

          
  
a=admin_panel()
a.create_group('wc')
a.add_device_to_group('wc', 'hom/wc/lamp/lamp1')
a.create_device('wc', 'lamp', 'lamp2')
a.create_group('living')
a.add_device_to_group('living', 'home/living/fan/fan3')
a.create_sensor('sensor1', 'wc', 3, 2536)
a.add_sensor_in_group('living',' home/living/tv/tv2')
print(a.groups)
a.displaying_groups()
print(a.get_status_in_device_type('lamp'))
print(a.groups)

        
